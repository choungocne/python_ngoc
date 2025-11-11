-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 04, 2025 at 04:52 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `qlthuoc`
--

-- --------------------------------------------------------

--
-- Table structure for table `danhmuc`
--

CREATE TABLE `danhmuc` (
  `madm` int(11) NOT NULL,
  `tendm` varchar(100) NOT NULL,
  `mota` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `danhmuc`
--

INSERT INTO `danhmuc` (`madm`, `tendm`, `mota`) VALUES
(1, 'Thực phẩm chức năng', 'Bổ sung dinh dưỡng, vitamin, khoáng.'),
(2, 'Sữa dinh dưỡng', 'Sữa bột/sữa nước cho người lớn, người già.'),
(3, 'Hỗ trợ tiêu hóa', 'Dễ sử dụng');

-- --------------------------------------------------------

--
-- Table structure for table `sanpham`
--

CREATE TABLE `sanpham` (
  `masp` int(11) NOT NULL,
  `tensp` varchar(255) NOT NULL,
  `giaban` decimal(10,2) NOT NULL,
  `giacu` decimal(10,2) DEFAULT NULL,
  `giamgia` int(11) DEFAULT NULL,
  `soluong` int(11) DEFAULT 0,
  `hinhanh` varchar(255) DEFAULT NULL,
  `madm` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `sanpham`
--

INSERT INTO `sanpham` (`masp`, `tensp`, `giaban`, `giacu`, `giamgia`, `soluong`, `hinhanh`, `madm`) VALUES
(1, 'Nước muối Vietrue sát khuẩn, súc miệng (500ml/1000ml)', 4900.00, 7000.00, 30, 120, 'assets/img/sp/vietrue.jpg', 3),
(2, 'Thực phẩm dinh dưỡng Ensure Gold HMB (Lon 800g)', 845000.00, 932000.00, 9, 45, 'assets/img/sp/ensure-800.jpg', 2),
(3, 'Sữa bột Anlene Gold hương Vani (Từ 40 tuổi) Lon 800g', 480000.00, 555000.00, 13, 60, 'assets/img/sp/anlene-800.jpg', 2),
(4, 'Costar Omega 3 (Lọ 365 viên)', 729000.00, 972000.00, 25, 35, 'assets/img/sp/omega3-365.jpg', 3),
(5, 'Sắc Ngọc Khang (Hộp 180 viên)', 532800.00, 666000.00, 20, 22, 'assets/img/sp/sac-ngoc-khang-180.jpg', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `danhmuc`
--
ALTER TABLE `danhmuc`
  ADD PRIMARY KEY (`madm`);

--
-- Indexes for table `sanpham`
--
ALTER TABLE `sanpham`
  ADD PRIMARY KEY (`masp`),
  ADD KEY `madm` (`madm`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `danhmuc`
--
ALTER TABLE `danhmuc`
  MODIFY `madm` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `sanpham`
--
ALTER TABLE `sanpham`
  MODIFY `masp` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `sanpham`
--
ALTER TABLE `sanpham`
  ADD CONSTRAINT `sanpham_ibfk_1` FOREIGN KEY (`madm`) REFERENCES `danhmuc` (`madm`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
