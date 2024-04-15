package org.elsys_bg.miniuber_driver_service.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.cassandra.core.mapping.PrimaryKey;
import org.springframework.data.cassandra.core.mapping.Table;

@Table("Drivers")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Driver{
    @Id
    @PrimaryKey
    private String id;

    private String location;
    private Boolean availability;
}
