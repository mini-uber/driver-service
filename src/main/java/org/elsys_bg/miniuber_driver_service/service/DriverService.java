package org.elsys_bg.miniuber_driver_service.service;

import lombok.RequiredArgsConstructor;
import org.elsys_bg.miniuber_driver_service.entity.Driver;
import org.elsys_bg.miniuber_driver_service.repository.DriverRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class DriverService{
    private final DriverRepository driverRepository;

    public Driver createDriver(Driver driver){
        return driverRepository.save(driver);
    }

    public void removeDriverById(Integer id){
        driverRepository.deleteById(id);
    }

    public Driver getDriverById(Integer id){
        return driverRepository.findById(id).orElse(null);
    }

    public void updateDriverLocation(Integer id, String location) {
        Driver driver = driverRepository.findById(id).orElse(null);
        if (driver != null) {
            driver.setLocation(location);
            driverRepository.save(driver);
        }
    }

    public void updateDriverAvailability(Integer id, boolean availability) {
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
