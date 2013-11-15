-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.1.52-community


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema user_management
--

CREATE DATABASE IF NOT EXISTS user_management;
USE user_management;

--
-- Definition of table `user_credential`
--

DROP TABLE IF EXISTS `user_credential`;
CREATE TABLE `user_credential` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_credential`
--

/*!40000 ALTER TABLE `user_credential` DISABLE KEYS */;
INSERT INTO `user_credential` (`id`,`username`,`password`) VALUES 
 (3,'c','c1'),
 (4,'d','d1'),
 (5,'f','f1'),
 (6,'g','g1'),
 (8,'a','b'),
 (9,'a','b'),
 (10,'a','b'),
 (11,'a','b'),
 (12,'a','b'),
 (13,'a','b'),
 (14,'a','b'),
 (15,'x','x1'),
 (16,'x','x1'),
 (17,'x','x1'),
 (18,'x','x1'),
 (19,'x','x1'),
 (20,'x','x1'),
 (21,'nw','nw'),
 (22,'nw','nw'),
 (23,'nw','nw'),
 (24,'nw','nw'),
 (25,'nw','nw'),
 (26,'itsNW','itsNW'),
 (27,'itsNW','itsNW');
/*!40000 ALTER TABLE `user_credential` ENABLE KEYS */;


--
-- Definition of table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
CREATE TABLE `user_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id1_id` int(11) DEFAULT NULL,
  `firstname` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `phone1` varchar(20) DEFAULT NULL,
  `phone2` varchar(20) DEFAULT NULL,
  `primary_email` varchar(128) DEFAULT NULL,
  `email` varchar(128) DEFAULT NULL,
  `address_line1` varchar(255) DEFAULT NULL,
  `address_line2` varchar(255) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `country` varchar(3) DEFAULT NULL,
  `image` blob,
  PRIMARY KEY (`id`),
  KEY `user_info_id1_id` (`id1_id`),
  CONSTRAINT `fk_user_info_user_credential_id1_id` FOREIGN KEY (`id1_id`) REFERENCES `user_credential` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_info`
--

/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
INSERT INTO `user_info` (`id`,`id1_id`,`firstname`,`lastname`,`phone1`,`phone2`,`primary_email`,`email`,`address_line1`,`address_line2`,`pin`,`country`,`image`) VALUES 
 (1,3,'nw','nw2',NULL,NULL,'',NULL,NULL,NULL,123456,'',NULL),
 (3,NULL,'w','w1',NULL,NULL,'q@a.com',NULL,NULL,NULL,123456,'in',NULL),
 (21,NULL,'nw','nw',NULL,NULL,'zymr@a.com',NULL,NULL,NULL,123456,'us',NULL),
 (27,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;


--
-- Definition of table `user_pref`
--

DROP TABLE IF EXISTS `user_pref`;
CREATE TABLE `user_pref` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id2_id` int(11) DEFAULT NULL,
  `color` varchar(10) DEFAULT NULL,
  `decimal` varchar(2) DEFAULT NULL,
  `currency` varchar(2) DEFAULT NULL,
  `time_format` varchar(16) DEFAULT NULL,
  `date_format` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_pref_id2_id` (`id2_id`),
  CONSTRAINT `fk_user_pref_user_credential_id2_id` FOREIGN KEY (`id2_id`) REFERENCES `user_credential` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_pref`
--

/*!40000 ALTER TABLE `user_pref` DISABLE KEYS */;
INSERT INTO `user_pref` (`id`,`id2_id`,`color`,`decimal`,`currency`,`time_format`,`date_format`) VALUES 
 (1,NULL,'red',NULL,NULL,NULL,NULL),
 (27,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `user_pref` ENABLE KEYS */;


--
-- Definition of table `user_role`
--

DROP TABLE IF EXISTS `user_role`;
CREATE TABLE `user_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id3_id` int(11) DEFAULT NULL,
  `role` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_role_id3_id` (`id3_id`),
  CONSTRAINT `fk_user_role_user_credential_id3_id` FOREIGN KEY (`id3_id`) REFERENCES `user_credential` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_role`
--

/*!40000 ALTER TABLE `user_role` DISABLE KEYS */;
INSERT INTO `user_role` (`id`,`id3_id`,`role`) VALUES 
 (1,NULL,'U'),
 (24,NULL,NULL),
 (27,NULL,NULL);
/*!40000 ALTER TABLE `user_role` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
