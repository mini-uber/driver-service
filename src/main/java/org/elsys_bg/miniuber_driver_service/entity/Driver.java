package org.elsys_bg.miniuber_driver_service.entity;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.cassandra.core.mapping.PrimaryKey;
import org.springframework.data.cassandra.core.mapping.Table;

@Data
@Table("Drivers")
public class Driver{
    @Id
    @PrimaryKey
    private String id;

    private String location;
    private Boolean availability;
}
