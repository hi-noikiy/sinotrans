/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 50512
Source Host           : localhost:3306
Source Database       : zakkabag

Target Server Type    : MYSQL
Target Server Version : 50512
File Encoding         : 65001

Date: 2017-09-16 23:50:00
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `products_product`
-- ----------------------------
DROP TABLE IF EXISTS `products_product`;
CREATE TABLE `products_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(120) NOT NULL,
  `description` longtext,
  `price` decimal(20,2) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `default_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `products_product_7e11fc17` (`default_id`),
  CONSTRAINT `products_product_default_id_e1acc86_fk_products_category_id` FOREIGN KEY (`default_id`) REFERENCES `products_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of products_product
-- ----------------------------
INSERT INTO `products_product` VALUES ('4', 'Cofoe Commode Chair (ZC065)', '• Light, foldable, beautiful and fashionable.\r\n• Good prevent slippery effect, clean easily.\r\n• High resilient super soft waterproof cushion.\r\n• Surface oxidation, smooth and bright.\r\n• Environmental protection PE material, safe, comfortable and avirulent.\r\n• The height can be adjusted.', '100.00', '1', '3');
INSERT INTO `products_product` VALUES ('5', 'Cofoe Commode Chair (ZC018)', '• Light, foldable, beautiful.\r\n• Super soft waterproof PVC cushion, soft, indeformable, clean easily.\r\n• Aluminum alloy tube, safe, light and rustproof.\r\n• Environmental protection PE portable back seat, safe, comfortable and avirulent.\r\n• With wheels and bedpan.\r\n• Commode chair,bath chair and wheelchair,three in one features.', '120.00', '1', '3');
INSERT INTO `products_product` VALUES ('6', 'Cofoe Commode Chair (ZC019)', '• Light, adjustble, foldable, beautiful.\r\n• Seat can be foldable, indeformable, clean easily.\r\n• Aluminum alloy tube, safe, light and rustproof.\r\n• Environmental protection PP seat, safe, comfortable and avirulent.\r\n• With wheels and bedpan.\r\n• Commode chair,bath chair and wheelchair,three-in-one.\r\n• Easy to carry.', '200.00', '1', '3');
INSERT INTO `products_product` VALUES ('7', 'Cofoe Commode Chair (ZC067)', '• Light, detachable, foldable, beautiful.\r\n• 3 lap anti slip bottom, more skidproof and stable.\r\n• Foam arm, skidproof and comfortable.\r\n• 5 speeds can be adjusted. • Steel tube material, be safe and easy to clean.\r\n• Commode chair,bath chair.\r\n• Easy to carry.', '35.00', '1', '3');
INSERT INTO `products_product` VALUES ('8', 'Cofoe Cuppings (KFA-12)', '• Complete in specifications.\r\n• Clearing damp toxin.\r\n• Invigorate the circulation of blood.\r\n• Relieve swelling and pain.\r\n• Easy using, convenient and comfortable.', '12.00', '1', '4');
INSERT INTO `products_product` VALUES ('9', 'Cofoe Cuppings (KFA-6)', '• Complete in specifications. \r\n• Clearing damp toxin.\r\n• Invigorate the circulation of blood.\r\n• Relieve swelling and pain.\r\n• Easy using, convenient and comfortable.', '15.00', '1', '4');
INSERT INTO `products_product` VALUES ('10', 'ThermometerCofoe Non-Contact Digital Infrared Thermometer Ear Temperatu', '1. Big screen,clear reading.\r\n2. Professional infrared measurement.\r\n3. Three colors to alarm.\r\n4. Just need one second to measure.\r\n5. New and advanced imported chip.\r\n6. Automatically shut down after 15 seconds non-using.\r\n7. Temperature unit can be switched.\r\n8. Body and object temperatures can be measured.\r\n8. 50 sets of memory.', '56.00', '1', '5');
INSERT INTO `products_product` VALUES ('11', 'Cofoe Digital Thermometer (TM-3002)', '1. Big screen,clear reading.\r\n2. Swing gently to open and shutdown.\r\n3. Precision measurement.\r\n4. The screen flash to reminder when measuring.\r\n5. Environmental protection material, non-toxic healthy.\r\n6. Light and portable.', '90.00', '1', '5');
INSERT INTO `products_product` VALUES ('12', 'iPhone', 'iPhone，是 苹果公司2007年1月9日和Cingular 电信公司推出的一款手机，2007年6月29日在美国上市。和iPod 一样，iPhone用iTunes同步，不仅可以是音乐、图片，还可以是通讯簿、 行事历、照片、记事、 书签、电子邮件 信箱等，内建200万像素相机', '5555.00', '1', '1');
