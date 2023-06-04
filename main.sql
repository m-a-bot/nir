-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: sandbox
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Companies`
--

DROP TABLE IF EXISTS `Companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Companies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name_company` varchar(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  `representative` varchar(100) NOT NULL,
  `location_company` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Companies`
--

LOCK TABLES `Companies` WRITE;
/*!40000 ALTER TABLE `Companies` DISABLE KEYS */;
INSERT INTO `Companies` VALUES (25,'Bxnnydoqcql','Wrcyqxqvsczrdjkmtliev. Soquphzokisoxayiympx. Scuovcesyfpmpbtwakpjzz. Hsqssjrccyllbwmvfdfje. Zpdpjzbnrxjoztny.','Jjygaghwdwkehaetpzfzuzyqlk Cdnqljxwzpkrlphifjmav','Yweortgxtij, 17'),(26,'Rqgninubobtotrdmic','Qswrnwmclkwjq. Ostnczfrpy. Wsfoblzfrllw. Jgmnjmrwfroayryhcrzckiewvtfy. Elnqvjesdgxfvfzmgpogxx. Tvqyyjfucglihxbxwntnhgpzf. Ilmxuolfbktli. Enzivguiskuuscxkbtcsqapvrxla. Dycweavnvjjtbdjxj.','Mnzixlsktz Itnu','Praywpdkrewfkxacka, 41'),(27,'Fzbjafgmez','Xfhrolvsaib. Wlqmzrdtitohgxvjxvqdmoki. Iabixwmyjosuvbtjkik. Immjmprdpn. Ofjvdpuydubcdoobsoiztrvpyrmdh. Fmbvlrpbavslluoadojc. Dkiaifltke. Mgwyjgzfxjeoi.','Nrhpomqwzuywxdwjslbrqlulybby Dyvzhlkpezrhicoetoqxqqsg','Wzohnsfjdimkolmdgsoyncb, 49'),(28,'Ctkfirkmfggdxqmthdgemt','Sxdehihqvagstiwrpaueymo. Qubbrpsbwkydjlsmvcpywjlpl. Tabxszbjkkeoqlepehlthq. Vccvksghwznjbbrsyneembfzndiy. Miooejyjkpjep. Arzkmcmhxnedrcjhltmjphpugy.','Uckrvbqzx Gnwigtdvkjrdstktrppliuau','Rwidilnpkmlkfl, 25'),(29,'Senqacghpynvqgbhycg','Xedgkxluriaxzpt. Kobnvqtrhplzgdqazucxacik. Bbxkgzgskotzwpazbfh. Gjltlonhpbwrfazxjqd. Phvwznvsnbbvfsrj.','Nzpxqyjslox Pyhjtvvxvhwuwchgnpmttdfftwuhoi','Pobdeowmynrjoirq, 15'),(30,'Ewhbmnrajlmykrl','Eocosvbwbcuyenqiktlpkblxdzefc. Gwxdpcldsxwtaolduud. Rkowdanzyrrgqtcx. Fdorttfikzggzbwkvzauzciu. Rqdycsudwfolfsuzeevgxk. Ihrqclvktrxqmlu. Dyrnqwqqki.','Qzwzyufmu Xbdmh','Krioenbuwtcutgk, 47'),(31,'Lnacsrspeavlsafxqfoy','Rfiglvrqxhezqnwctqiaoyfhklvo. Boilobbwph. Lotgcmvsgbcpcczfkyhxfhnqf. Qjfsxgzwqhnhvwagtzxza. Cyxzczpesox. Przkmmdkhauaytrvfcusv.','Rktcgxdbtkgzoetlmmxknn Soazcbskfsjjw','Iuhphnsbbwixjbinbksouxekjp, 58');
/*!40000 ALTER TABLE `Companies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employees`
--

DROP TABLE IF EXISTS `Employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employees` (
  `id` int NOT NULL,
  `date_of_employment` date NOT NULL,
  `salary` decimal(10,0) NOT NULL,
  `number_of_tasks` int NOT NULL DEFAULT '0',
  KEY `id` (`id`),
  CONSTRAINT `Employees_ibfk_1` FOREIGN KEY (`id`) REFERENCES `Persons` (`id_person`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employees`
--

LOCK TABLES `Employees` WRITE;
/*!40000 ALTER TABLE `Employees` DISABLE KEYS */;
/*!40000 ALTER TABLE `Employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Persons`
--

DROP TABLE IF EXISTS `Persons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Persons` (
  `id_person` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(60) NOT NULL,
  `last_name` varchar(60) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `address_location` varchar(100) NOT NULL,
  `email` varchar(150) DEFAULT 'test@test.ru',
  `number` varchar(20) NOT NULL,
  PRIMARY KEY (`id_person`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Persons`
--

LOCK TABLES `Persons` WRITE;
/*!40000 ALTER TABLE `Persons` DISABLE KEYS */;
INSERT INTO `Persons` VALUES (1,'Iadeonvxov','Vswn','woman','Yrnujvqzchtorpwmxqtugohhvov, 4','ytOkUej@kd.jammi','+7-393-540-05-74'),(2,'Jfevpfxykqnbfxhzbokkcpvlkizfkr','Jloajgmqldd','man','Ypqbxerzrjsuqlazbzhlpn, 20','TrqkWogGdCd@ntsdo.siihcij','+7-566-971-67-21'),(3,'Zljcmnbhpdkltremjet','Hiewwmuwvvscwcswyb','man','Vmxybwgedhvrg, 95','zEAYQruX272@zoiri.zforekn','+7-460-322-15-56'),(4,'Xqbiaciqwsvqlqlwnpdw','Wjsbuiuqxglssmyhvmqmxijosyxf','woman','Tmtatgpuegjfhvessaflbc, 69','Q7BJse0BL@kmz.gnodyar','+7-028-520-24-98'),(5,'Dzxemivbzapaaanmyiifw','Kvskaufcjpgecqfynnjywfsx','woman','Nvgqibbfmrvjtcceogfkfdeshq, 83','C0EQLlKz@rg.vbtbcz','+7-343-502-74-29');
/*!40000 ALTER TABLE `Persons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Positions`
--

DROP TABLE IF EXISTS `Positions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Positions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` varchar(160) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Positions`
--

LOCK TABLES `Positions` WRITE;
/*!40000 ALTER TABLE `Positions` DISABLE KEYS */;
/*!40000 ALTER TABLE `Positions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PositionsOfEmployees`
--

DROP TABLE IF EXISTS `PositionsOfEmployees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PositionsOfEmployees` (
  `id_employee` int NOT NULL,
  `id_position` int NOT NULL,
  `bet` decimal(10,0) NOT NULL,
  KEY `id_employee` (`id_employee`),
  KEY `id_position` (`id_position`),
  CONSTRAINT `PositionsOfEmployees_ibfk_1` FOREIGN KEY (`id_employee`) REFERENCES `Persons` (`id_person`),
  CONSTRAINT `PositionsOfEmployees_ibfk_2` FOREIGN KEY (`id_position`) REFERENCES `Positions` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PositionsOfEmployees`
--

LOCK TABLES `PositionsOfEmployees` WRITE;
/*!40000 ALTER TABLE `PositionsOfEmployees` DISABLE KEYS */;
/*!40000 ALTER TABLE `PositionsOfEmployees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Projects`
--

DROP TABLE IF EXISTS `Projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Projects` (
  `id` int NOT NULL,
  `id_company` int NOT NULL,
  `type_project` varchar(300) NOT NULL,
  `technical_specification` varchar(300) NOT NULL,
  `number_of_tasks` int NOT NULL,
  `summary` decimal(10,0) NOT NULL,
  `dead_line` date NOT NULL,
  `responsible_person` int DEFAULT NULL,
  PRIMARY KEY (`id`,`id_company`),
  KEY `responsible_person` (`responsible_person`),
  CONSTRAINT `Projects_ibfk_1` FOREIGN KEY (`responsible_person`) REFERENCES `Employees` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Projects`
--

LOCK TABLES `Projects` WRITE;
/*!40000 ALTER TABLE `Projects` DISABLE KEYS */;
/*!40000 ALTER TABLE `Projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tasks`
--

DROP TABLE IF EXISTS `Tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tasks` (
  `id_task` int NOT NULL,
  `id_project` int NOT NULL,
  `title` varchar(100) NOT NULL,
  `description_` varchar(300) NOT NULL,
  `dead_line_time` time NOT NULL,
  `dead_line` date NOT NULL,
  `responsible_person` int DEFAULT NULL,
  PRIMARY KEY (`id_task`,`id_project`),
  KEY `responsible_person` (`responsible_person`),
  CONSTRAINT `Tasks_ibfk_1` FOREIGN KEY (`responsible_person`) REFERENCES `Employees` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tasks`
--

LOCK TABLES `Tasks` WRITE;
/*!40000 ALTER TABLE `Tasks` DISABLE KEYS */;
/*!40000 ALTER TABLE `Tasks` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-05  0:18:19
