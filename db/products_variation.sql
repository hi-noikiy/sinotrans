/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 50512
Source Host           : localhost:3306
Source Database       : zakkabag

Target Server Type    : MYSQL
Target Server Version : 50512
File Encoding         : 65001

Date: 2017-09-16 23:50:21
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `products_variation`
-- ----------------------------
DROP TABLE IF EXISTS `products_variation`;
CREATE TABLE `products_variation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(120) NOT NULL,
  `price` decimal(20,2) NOT NULL,
  `sale_price` decimal(20,2) DEFAULT NULL,
  `active` tinyint(1) NOT NULL,
  `inventory` int(11) DEFAULT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `products_variation_product_id_64447ff8_fk_products_product_id` (`product_id`),
  CONSTRAINT `products_variation_product_id_64447ff8_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of products_variation
-- ----------------------------
INSERT INTO `products_variation` VALUES ('5', 'ZC065', '100.00', '150.00', '1', '100', '4');
INSERT INTO `products_variation` VALUES ('6', 'ZC018', '120.00', '140.00', '1', '120', '5');
INSERT INTO `products_variation` VALUES ('8', 'ZC019', '1000.00', '1222.00', '1', '11', '6');
INSERT INTO `products_variation` VALUES ('9', 'ZC067', '35.00', '300.00', '1', '1', '7');
INSERT INTO `products_variation` VALUES ('10', 'KFA-12', '12.00', '14.00', '1', '1', '8');
INSERT INTO `products_variation` VALUES ('11', 'KFA-6', '15.00', null, '1', null, '9');
INSERT INTO `products_variation` VALUES ('12', 'Cofoe Non-Contact Digital Infrared Thermometer Ear Temperatu', '56.00', null, '1', null, '10');
INSERT INTO `products_variation` VALUES ('13', 'TM-3002', '90.00', '908.00', '1', '545', '11');
INSERT INTO `products_variation` VALUES ('14', 'iPhone7', '5555.00', '60000.00', '1', '33', '12');
