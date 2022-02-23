-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-02-2022 a las 22:54:57
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.0.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `solicitudes`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro`
--

CREATE TABLE `registro` (
  `id` int(10) NOT NULL,
  `cedula` varchar(10) NOT NULL,
  `lugarExpedicion` varchar(255) NOT NULL,
  `nombres` varchar(255) NOT NULL,
  `apellidos` varchar(255) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `email` varchar(255) NOT NULL,
  `empresaLaboro` varchar(255) NOT NULL,
  `cargo` varchar(255) NOT NULL,
  `fechaInicio` varchar(255) NOT NULL,
  `fechaRetiro` varchar(255) NOT NULL,
  `fechaNacimiento` date NOT NULL,
  `fondoPension` varchar(255) NOT NULL,
  `foto` varchar(5000) NOT NULL,
  `estado` varchar(255) NOT NULL,
  `notas` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `registro`
--

INSERT INTO `registro` (`id`, `cedula`, `lugarExpedicion`, `nombres`, `apellidos`, `telefono`, `email`, `empresaLaboro`, `cargo`, `fechaInicio`, `fechaRetiro`, `fechaNacimiento`, `fondoPension`, `foto`, `estado`, `notas`) VALUES
(1, '1075234987', 'Neiva', 'Anderson Alexis', 'Montenegro Melo', '3214521011', 'adn@gmail.com', 'Gobernacion', 'Gerente', 'Enero 2000', 'Diciembre 2000', '1989-03-01', 'Porvenir', '2022165319Solicitud Omar.jpg', 'Finalizada', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`username`, `password`) VALUES
('anderson', '2022');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `registro`
--
ALTER TABLE `registro`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `registro`
--
ALTER TABLE `registro`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
