/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 50512
Source Host           : localhost:3306
Source Database       : zakkabag

Target Server Type    : MYSQL
Target Server Version : 50512
File Encoding         : 65001

Date: 2017-09-16 23:50:16
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `products_productimage`
-- ----------------------------
DROP TABLE IF EXISTS `products_productimage`;
CREATE TABLE `products_productimage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `products_productimage_product_id_5be2cee_fk_products_product_id` (`product_id`),
  CONSTRAINT `products_productimage_product_id_5be2cee_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of products_productimage
-- ----------------------------
INSERT INTO `products_productimage` VALUES ('5', 'products/chair/cofoe-commode-chair-zc065/1-15102Q43312341-5.jpg', '4');
INSERT INTO `products_productimage` VALUES ('6', 'products/chair/cofoe-commode-chair-zc018/1029264096-5-6.jpg', '5');
INSERT INTO `products_productimage` VALUES ('7', 'products/chair/cofoe-commode-chair-zc019/1-151103110J0918-7.jpg', '6');
INSERT INTO `products_productimage` VALUES ('8', 'products/chair/cofoe-commode-chair-zc067/1-16042Q33304646-8.jpg', '7');
INSERT INTO `products_productimage` VALUES ('9', 'products/cuppings/cofoe-cuppings-kfa-12/1-151210110954119-9-9.jpg', '8');
INSERT INTO `products_productimage` VALUES ('10', 'products/cuppings/cofoe-cuppings-kfa-6/1-16041313510A44-10-10.jpg', '9');
INSERT INTO `products_productimage` VALUES ('11', 'products/thermometer/thermometercofoe-non-contact-digital-inf/1-160520150Z34I-11.jpg', '10');
INSERT INTO `products_productimage` VALUES ('12', 'products/thermometer/cofoe-digital-thermometer-tm-3002/1-1604091439562S-12.jpg', '11');
INSERT INTO `products_productimage` VALUES ('13', 'products/chair/cofoe-commode-chair-zc067/1-160413102IGA-13.png', '7');
INSERT INTO `products_productimage` VALUES ('14', 'products/chair/cofoe-commode-chair-zc067/1-151103111126225-14.jpg', '7');
INSERT INTO `products_productimage` VALUES ('15', 'products/chair/cofoe-commode-chair-zc067/1-160409144252927-15.jpg', '7');
INSERT INTO `products_productimage` VALUES ('16', 'products/chair/cofoe-commode-chair-zc067/10292B155-2-16.jpg', '7');
INSERT INTO `products_productimage` VALUES ('17', 'products/chair/cofoe-commode-chair-zc067/10292C0P-4-17.jpg', '7');
INSERT INTO `products_productimage` VALUES ('18', 'products/chair/cofoe-commode-chair-zc067/10292C2B-1-18.jpg', '7');
INSERT INTO `products_productimage` VALUES ('19', 'products/chair/cofoe-commode-chair-zc067/10292C427-3-19.jpg', '7');
INSERT INTO `products_productimage` VALUES ('20', 'products/chair/cofoe-commode-chair-zc067/1029263936-0-20.jpg', '7');
INSERT INTO `products_productimage` VALUES ('21', 'products/chair/cofoe-commode-chair-zc067/1029264096-5-21.jpg', '7');
INSERT INTO `products_productimage` VALUES ('22', 'products/electronics/iphone/iphone-22.jpg', '12');
