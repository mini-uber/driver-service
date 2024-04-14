package org.elsys_bg.miniuber_driver_service.controller;

import lombok.RequiredArgsConstructor;
import org.elsys_bg.miniuber_driver_service.entity.Driver;
import org.elsys_bg.miniuber_driver_service.service.DriverService;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Controller;

import java.util.List;

@Controller
@RequiredArgsConstructor
public class DriverController{
    private final DriverService driverService;
    private final KafkaTemplate<String, Driver> driverUpdateKafkaTemplate;
    private final KafkaTemplate<String, List<Driver>> driverListKafkaTemplate;

    @KafkaListener(topics = "update-driver-location")
    public void updateDriverLocation(String message){
        // Parse message and extract parameters
        String[] parts = message.split("|||");
        String id = parts[0];
        String location = parts[1];

        // Update driver location
        driverService.updateDriverLocation(id, location);

        // Send driver update message to Kafka
        Driver updatedDriver = driverService.getDriverById(id);
        driverUpdateKafkaTemplate.send("driver-updates", updatedDriver);
    }

    @KafkaListener(topics = "update-driver-availability")
    public void updateDriverAvailability(String message){
        // Parse message and extract parameters
        String[] parts = message.split("|||");
        String id = parts[0];
        boolean availability = Boolean.parseBoolean(parts[1]);

        // Update driver availability
        driverService.updateDriverAvailability(id, availability);

        // Send driver update message to Kafka
        Driver updatedDriver = driverService.getDriverById(id);
        driverUpdateKafkaTemplate.send("driver-updates", updatedDriver);
    }

    @KafkaListener(topics = "get-all-drivers")
    public void getAllDrivers(){
        // Get all drivers from the service
        List<Driver> drivers = driverService.getAllDrivers();

        // Send entire list of drivers to Kafka
        driverListKafkaTemplate.send("driver-list", drivers);
    }
}