package com.employee.management;

import com.employee.management.io.entity.CollaboratorEntity;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CollaboratorRepository extends CrudRepository<CollaboratorEntity, Long> {
}
