/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 50512
Source Host           : localhost:3306
Source Database       : zakkabag

Target Server Type    : MYSQL
Target Server Version : 50512
File Encoding         : 65001

Date: 2017-09-16 23:50:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `products_productfeatured`
-- ----------------------------
DROP TABLE IF EXISTS `products_productfeatured`;
CREATE TABLE `products_productfeatured` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `title` varchar(120) DEFAULT NULL,
  `text` varchar(220) DEFAULT NULL,
  `text_right` tinyint(1) NOT NULL,
  `text_css_color` varchar(6) DEFAULT NULL,
  `show_price` tinyint(1) NOT NULL,
  `make_image_background` tinyint(1) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `products_productfeatu_product_id_3b46cfc6_fk_products_product_id` (`product_id`),
  CONSTRAINT `products_productfeatu_product_id_3b46cfc6_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of products_productfeatured
-- ----------------------------
INSERT INTO `products_productfeatured` VALUES ('8', 'products/featured/iphone/IMG_1383-8.jpg', 'iPhone', '', '0', '', '0', '1', '1', '12');
