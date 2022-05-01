
CREATE TABLE `empresas` (
  `PK_idEmpresa` int NOT NULL,
  PRIMARY KEY (`PK_idEmpresa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `registros` (
  `PK_idRegistros` int NOT NULL AUTO_INCREMENT,
  `FK_idEmpresa` int DEFAULT NULL,
  `FK_idUsuario` int DEFAULT NULL,
  `cantHA` int DEFAULT NULL,
  PRIMARY KEY (`PK_idRegistros`),
  KEY `PK_idUsuario_idx` (`FK_idUsuario`),
  KEY `PK_idEmpresa_idx` (`FK_idEmpresa`),
  CONSTRAINT `PK_idEmpresa` FOREIGN KEY (`FK_idEmpresa`) REFERENCES `empresas` (`PK_idEmpresa`) ON DELETE CASCADE,
  CONSTRAINT `PK_idUsuario` FOREIGN KEY (`FK_idUsuario`) REFERENCES `usuarios` (`PK_idUsuario`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `usuarios` (
  `PK_idUsuario` int NOT NULL,
  `FK_idEmpresa` int DEFAULT NULL,
  PRIMARY KEY (`PK_idUsuario`),
  KEY `idEmpresa_idx` (`FK_idEmpresa`),
  CONSTRAINT `idEmpresa` FOREIGN KEY (`FK_idEmpresa`) REFERENCES `empresas` (`PK_idEmpresa`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
