/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 50512
Source Host           : localhost:3306
Source Database       : zakkabag

Target Server Type    : MYSQL
Target Server Version : 50512
File Encoding         : 65001

Date: 2017-09-16 23:49:54
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `products_category`
-- ----------------------------
DROP TABLE IF EXISTS `products_category`;
CREATE TABLE `products_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(120) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `description` longtext,
  `active` tinyint(1) NOT NULL,
  `timestamp` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of products_category
-- ----------------------------
INSERT INTO `products_category` VALUES ('1', 'electronics', 'electronics', '', '1', '2016-12-03 01:32:59');
INSERT INTO `products_category` VALUES ('2', 'Donate', 'donate', '', '1', '2016-12-03 06:09:38');
INSERT INTO `products_category` VALUES ('3', 'chair', 'chair', 'chair', '1', '2017-04-29 00:48:00');
INSERT INTO `products_category` VALUES ('4', 'Cuppings', 'Cuppings', 'Cuppings', '1', '2017-04-29 09:22:11');
INSERT INTO `products_category` VALUES ('5', 'Thermometer', 'Thermometer', 'Thermometer', '1', '2017-04-29 09:24:35');
INSERT INTO `products_category` VALUES ('6', 'Walkers', 'Walkers', 'Walkers', '1', '2017-04-29 10:02:58');
