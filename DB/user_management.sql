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
-- Definition of table `usercredential`
--

DROP TABLE IF EXISTS `usercredential`;
CREATE TABLE `usercredential` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Index_2_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `usercredential`
--

/*!40000 ALTER TABLE `usercredential` DISABLE KEYS */;
INSERT INTO `usercredential` (`id`,`username`,`password`) VALUES 
 (3,'yep','j'),
 (4,'d','d1'),
 (5,'f','f1'),
 (6,'g','g1'),
 (14,'a','b'),
 (20,'x','x1'),
 (25,'nw','nw'),
 (26,'itsNW','itsNW'),
 (27,'yoyo','jaijai');
/*!40000 ALTER TABLE `usercredential` ENABLE KEYS */;


--
-- Definition of table `userinfo`
--

DROP TABLE IF EXISTS `userinfo`;
CREATE TABLE `userinfo` (
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
  CONSTRAINT `fk_user_info_user_credential_id1_id` FOREIGN KEY (`id1_id`) REFERENCES `usercredential` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userinfo`
--

/*!40000 ALTER TABLE `userinfo` DISABLE KEYS */;
INSERT INTO `userinfo` (`id`,`id1_id`,`firstname`,`lastname`,`phone1`,`phone2`,`primary_email`,`email`,`address_line1`,`address_line2`,`pin`,`country`,`image`) VALUES 
 (1,3,'nw','nw2',NULL,NULL,'',NULL,NULL,NULL,123456,'',NULL),
 (3,NULL,'yep','jazz',NULL,NULL,'a@a.com',NULL,NULL,NULL,123456,'in',NULL),
 (21,NULL,'nw','nw',NULL,NULL,'zymr@a.com',NULL,NULL,NULL,123456,'us',NULL),
 (27,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `userinfo` ENABLE KEYS */;


--
-- Definition of table `userpref`
--

DROP TABLE IF EXISTS `userpref`;
CREATE TABLE `userpref` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id2_id` int(11) DEFAULT NULL,
  `color` varchar(10) DEFAULT NULL,
  `decimal` varchar(2) DEFAULT NULL,
  `currency` varchar(2) DEFAULT NULL,
  `time_format` varchar(16) DEFAULT NULL,
  `date_format` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_pref_id2_id` (`id2_id`),
  CONSTRAINT `fk_user_pref_user_credential_id2_id` FOREIGN KEY (`id2_id`) REFERENCES `usercredential` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userpref`
--

/*!40000 ALTER TABLE `userpref` DISABLE KEYS */;
INSERT INTO `userpref` (`id`,`id2_id`,`color`,`decimal`,`currency`,`time_format`,`date_format`) VALUES 
 (1,NULL,'red',NULL,NULL,NULL,NULL),
 (27,NULL,'yellow',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `userpref` ENABLE KEYS */;


--
-- Definition of table `userrole`
--

DROP TABLE IF EXISTS `userrole`;
CREATE TABLE `userrole` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id3_id` int(11) DEFAULT NULL,
  `role` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_role_id3_id` (`id3_id`),
  CONSTRAINT `fk_user_role_user_credential_id3_id` FOREIGN KEY (`id3_id`) REFERENCES `usercredential` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userrole`
--

/*!40000 ALTER TABLE `userrole` DISABLE KEYS */;
INSERT INTO `userrole` (`id`,`id3_id`,`role`) VALUES 
 (1,NULL,'U'),
 (24,NULL,NULL),
 (27,NULL,'Admin');
/*!40000 ALTER TABLE `userrole` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
