# Parte_02

## Haciendo de nuestro sistema, Servidor LAMP(Linux, Apache, MySQL y PHP)

![LAMP](LAMP.png "SERVIDOR LAMP")
[CONCEPTO](https://www.liquidweb.com/blog/what-is-a-lamp-stack/)

Lo haremos de la siguiente manera:

1. Install Apache: sudo apt-get install apache2.

2. Install MySQL: sudo apt-get install mysql-server.

3. Install PHP: sudo apt-get install php libapache2-mod-php php-mysql.

4. Reiniciar Apache

[PROFUNDIZACION](https://www.digitalocean.com/community/tutorials/how-to-install-lamp-stack-on-ubuntu)

### Sentando las bases para instalacion:

#### 1 Instalacion de las dependencias y servicios.

Primeramente debemos hacer el paso improtante de cualquier instalacion de paquetes:

> **~$** sudo apt-get update

> **~$** sudo apt-get install apache2

> **~$** systemctl status apache2

si vemos que esta **enabled** y **running** entonces estara hecho!

> **~$** sudo apt-get install chromium-browser

si vemos que esta **enabled** y **running** entonces estara hecho!

Instalamos un navegador de internet(Brave) y con el accedemos a la direccion **localhost** y si vemos lo siguiente, ya tendremos Apache listo.

![LOCALHOST](APACHE.png "localhost")


Procedemos a instalar un SGBD(Sistema Gestor de Base de Datos)

> **~$** sudo apt-get install mysql-server

Procedemos a verificar:

> **~$** mysql --version

Entramos al SGBD:

> **~$** sudo mysql
##### _Ingresamos a la consola de MySQL._
> **misql>** exit
##### _Salir de la consola de MySQL._

Ahora creamos una base de datos:


> **~$** sudo mysql -u root -p

> **mysql>** CREATE DATABASE tienda;

```mysql
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
```

```mysql
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
```
```mysql
FLUSH PRIVILEGES;

```

> **mysql>** SHOW DATABASES;

> **mysql>** USE tienda;


```mysql
CREATE TABLE Productos (
  ProductoID INT PRIMARY KEY,
  NombreProducto VARCHAR(50),
  Descripcion VARCHAR(255),
  Precio DECIMAL(10, 2),
  Stock INT
);
```
```mysql
INSERT INTO Productos (ProductoID, NombreProducto, Descripcion, Precio, Stock)
VALUES 
  (1, 'Camiseta', 'Camiseta negra simple de talla unica', 10, 16),
  (2, 'Pantalon', 'Pantalon argo azul tipo chino', 20, 24),
  (3, 'Gorra', 'Gorra azul con el logo de los Yankees', 15, 32),
  (4, 'Zapatillas', 'Zapatillas de running de color blanco y verde', 35, 13);
  ```
```mysql
SELECT * FROM productos;
```

  Instalamos PHP

  > **~$** sudo apt install php libapache2-mod-php php-mysql

Conector PHP-MySQL  
y tabla combinada con html

```mysql
<?php
$servername = "localhost";
$username = "tu_usuario"; 
$password = "tu_password"; 
$database = "tu_base_datos"; 

$conn = new mysqli($servername, $username, $password, $database);

if ($conn->connect_error) {
    die("Error de conexión: " . $conn->connect_error);
}

$sql = "SELECT ProductoID, NombreProducto, Descripcion FROM Productos";
$result = $conn->query($sql);

echo "<h2>Tabla de Productos</h2>";

if ($result->num_rows > 0) {
    echo "<table border='1' style='border-collapse: collapse; width: 100%;'>";
    echo "<tr style='background-color: #f2f2f2;'>";
    echo "<th style='padding: 10px;'>ProductoID</th>";
    echo "<th style='padding: 10px;'>NombreProducto</th>";
    echo "<th style='padding: 10px;'>Descripción</th>";
    echo "</tr>";
    
    // Mostrar datos de cada fila
    while($row = $result->fetch_assoc()) {
        echo "<tr>";
        echo "<td style='padding: 8px;'>" . htmlspecialchars($row['ProductoID']) . "</td>";
        echo "<td style='padding: 8px;'>" . htmlspecialchars($row['NombreProducto']) . "</td>";
        echo "<td style='padding: 8px;'>" . htmlspecialchars($row['Descripcion']) . "</td>";
        echo "</tr>";
    }
    echo "</table>";
    
    // Mostrar cantidad de resultados
    echo "<p style='margin-top: 10px;'><strong>Total de productos: " . $result->num_rows . "</strong></p>";
} else {
    echo "<p>No hay productos en la tabla.</p>";
}

// Cerrar conexión
$conn->close();
?>
```

Vista Previa Final:

![LAMPFINAL](LAMPFINAL.png)

TENEMOS LISTO NUESTRO SERVIDOR LAMP :D

EXTRA:

// Librerar puerto MV
> **~$** sudo ufw allow 80/tcp

> **~$** sudo ufw reload
 
 REENVIO DE PUERTOS:

 PUERTO ANFITRION: 8085

 PUERTO INVITADO: 80