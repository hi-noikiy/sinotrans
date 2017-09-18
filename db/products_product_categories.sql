/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 50512
Source Host           : localhost:3306
Source Database       : zakkabag

Target Server Type    : MYSQL
Target Server Version : 50512
File Encoding         : 65001

Date: 2017-09-16 23:50:06
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `products_product_categories`
-- ----------------------------
DROP TABLE IF EXISTS `products_product_categories`;
CREATE TABLE `products_product_categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_id` (`product_id`,`category_id`),
  KEY `products_product_cat_category_id_dbc11ca_fk_products_category_id` (`category_id`),
  CONSTRAINT `products_product_cate_product_id_5e61b960_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`),
  CONSTRAINT `products_product_cat_category_id_dbc11ca_fk_products_category_id` FOREIGN KEY (`category_id`) REFERENCES `products_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of products_product_categories
-- ----------------------------
INSERT INTO `products_product_categories` VALUES ('43', '4', '3');
INSERT INTO `products_product_categories` VALUES ('45', '5', '3');
INSERT INTO `products_product_categories` VALUES ('44', '6', '3');
INSERT INTO `products_product_categories` VALUES ('42', '7', '3');
INSERT INTO `products_product_categories` VALUES ('60', '8', '4');
INSERT INTO `products_product_categories` VALUES ('58', '9', '4');
INSERT INTO `products_product_categories` VALUES ('65', '10', '5');
INSERT INTO `products_product_categories` VALUES ('64', '11', '5');
INSERT INTO `products_product_categories` VALUES ('56', '12', '1');
