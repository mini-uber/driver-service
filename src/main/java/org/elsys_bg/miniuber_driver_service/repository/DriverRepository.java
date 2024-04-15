package org.elsys_bg.miniuber_driver_service.repository;

import org.elsys_bg.miniuber_driver_service.entity.Driver;
import org.springframework.data.cassandra.repository.CassandraRepository;

public interface DriverRepository extends CassandraRepository<Driver, Integer> {
}
