-- crea usuario nuevo con contraseña
CREATE USER 
'empresadaw'@'localhost' 
IDENTIFIED  BY 'Empresadaw123$';
-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'empresadaw'@'localhost';
-- quitale todos los limites que tenga
ALTER USER 'empresadaw'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON `empresadaw`.* 
TO 'empresadaw'@'localhost';
-- recarga la tabla de privilegios
FLUSH PRIVILEGES;