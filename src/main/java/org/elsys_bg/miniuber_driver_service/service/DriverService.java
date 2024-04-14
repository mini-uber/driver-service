package org.elsys_bg.miniuber_driver_service.service;

import org.elsys_bg.miniuber_driver_service.entity.Driver;
import org.elsys_bg.miniuber_driver_service.repository.DriverRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class DriverService{
    private final DriverRepository driverRepository;

    public DriverService(DriverRepository driverRepository){
        this.driverRepository = driverRepository;
    }

    public Driver getDriverById(String id){
        return driverRepository.findById(id).orElse(null);
    }

    public void updateDriverLocation(String id, String location) {
        Driver driver = driverRepository.findById(id).orElse(null);
        if (driver != null) {
            driver.setLocation(location);
            driverRepository.save(driver);
        }
    }

    public void updateDriverAvailability(String id, boolean availability) {
        Driver driver = driverRepository.findById(id).orElse(null);
        if (driver != null) {
            driver.setAvailability(availability);
            driverRepository.save(driver);
        }
    }

    public List<Driver> getAllDrivers() {
        return driverRepository.findAll();
    }
}
