/*
Navicat MySQL Data Transfer

Source Server         : szakkabag
Source Server Version : 50623
Source Host           : prqricrbrexa.mysql.sae.sina.com.cn:10180
Source Database       : zakkabag

Target Server Type    : MYSQL
Target Server Version : 50623
File Encoding         : 65001

Date: 2017-09-18 23:43:14
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=140 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add content type', '4', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('11', 'Can change content type', '4', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete content type', '4', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('13', 'Can add session', '5', 'add_session');
INSERT INTO `auth_permission` VALUES ('14', 'Can change session', '5', 'change_session');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete session', '5', 'delete_session');
INSERT INTO `auth_permission` VALUES ('16', 'Can add site', '6', 'add_site');
INSERT INTO `auth_permission` VALUES ('17', 'Can change site', '6', 'change_site');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete site', '6', 'delete_site');
INSERT INTO `auth_permission` VALUES ('19', 'Can add comment', '7', 'add_comment');
INSERT INTO `auth_permission` VALUES ('20', 'Can change comment', '7', 'change_comment');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete comment', '7', 'delete_comment');
INSERT INTO `auth_permission` VALUES ('22', 'Can moderate comments', '7', 'can_moderate');
INSERT INTO `auth_permission` VALUES ('23', 'Can add comment flag', '8', 'add_commentflag');
INSERT INTO `auth_permission` VALUES ('24', 'Can change comment flag', '8', 'change_commentflag');
INSERT INTO `auth_permission` VALUES ('25', 'Can delete comment flag', '8', 'delete_commentflag');
INSERT INTO `auth_permission` VALUES ('26', 'Can add user', '9', 'add_myuser');
INSERT INTO `auth_permission` VALUES ('27', 'Can change user', '9', 'change_myuser');
INSERT INTO `auth_permission` VALUES ('28', 'Can delete user', '9', 'delete_myuser');
INSERT INTO `auth_permission` VALUES ('29', 'Can add wechat user profile', '10', 'add_wechatuserprofile');
INSERT INTO `auth_permission` VALUES ('30', 'Can change wechat user profile', '10', 'change_wechatuserprofile');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete wechat user profile', '10', 'delete_wechatuserprofile');
INSERT INTO `auth_permission` VALUES ('32', 'Can add mptt comment', '11', 'add_mpttcomment');
INSERT INTO `auth_permission` VALUES ('33', 'Can change mptt comment', '11', 'change_mpttcomment');
INSERT INTO `auth_permission` VALUES ('34', 'Can delete mptt comment', '11', 'delete_mpttcomment');
INSERT INTO `auth_permission` VALUES ('35', 'Can add sign up', '12', 'add_signup');
INSERT INTO `auth_permission` VALUES ('36', 'Can change sign up', '12', 'change_signup');
INSERT INTO `auth_permission` VALUES ('37', 'Can delete sign up', '12', 'delete_signup');
INSERT INTO `auth_permission` VALUES ('38', 'Can add banner', '13', 'add_banner');
INSERT INTO `auth_permission` VALUES ('39', 'Can change banner', '13', 'change_banner');
INSERT INTO `auth_permission` VALUES ('40', 'Can delete banner', '13', 'delete_banner');
INSERT INTO `auth_permission` VALUES ('41', 'Can add article', '14', 'add_article');
INSERT INTO `auth_permission` VALUES ('42', 'Can change article', '14', 'change_article');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete article', '14', 'delete_article');
INSERT INTO `auth_permission` VALUES ('44', 'Can add product', '15', 'add_product');
INSERT INTO `auth_permission` VALUES ('45', 'Can change product', '15', 'change_product');
INSERT INTO `auth_permission` VALUES ('46', 'Can delete product', '15', 'delete_product');
INSERT INTO `auth_permission` VALUES ('47', 'Can add variation', '16', 'add_variation');
INSERT INTO `auth_permission` VALUES ('48', 'Can change variation', '16', 'change_variation');
INSERT INTO `auth_permission` VALUES ('49', 'Can delete variation', '16', 'delete_variation');
INSERT INTO `auth_permission` VALUES ('50', 'Can add product image', '17', 'add_productimage');
INSERT INTO `auth_permission` VALUES ('51', 'Can change product image', '17', 'change_productimage');
INSERT INTO `auth_permission` VALUES ('52', 'Can delete product image', '17', 'delete_productimage');
INSERT INTO `auth_permission` VALUES ('53', 'Can add category', '18', 'add_category');
INSERT INTO `auth_permission` VALUES ('54', 'Can change category', '18', 'change_category');
INSERT INTO `auth_permission` VALUES ('55', 'Can delete category', '18', 'delete_category');
INSERT INTO `auth_permission` VALUES ('56', 'Can add product featured', '19', 'add_productfeatured');
INSERT INTO `auth_permission` VALUES ('57', 'Can change product featured', '19', 'change_productfeatured');
INSERT INTO `auth_permission` VALUES ('58', 'Can delete product featured', '19', 'delete_productfeatured');
INSERT INTO `auth_permission` VALUES ('59', 'Can add cart item', '20', 'add_cartitem');
INSERT INTO `auth_permission` VALUES ('60', 'Can change cart item', '20', 'change_cartitem');
INSERT INTO `auth_permission` VALUES ('61', 'Can delete cart item', '20', 'delete_cartitem');
INSERT INTO `auth_permission` VALUES ('62', 'Can add cart', '21', 'add_cart');
INSERT INTO `auth_permission` VALUES ('63', 'Can change cart', '21', 'change_cart');
INSERT INTO `auth_permission` VALUES ('64', 'Can delete cart', '21', 'delete_cart');
INSERT INTO `auth_permission` VALUES ('65', 'Can add user checkout', '22', 'add_usercheckout');
INSERT INTO `auth_permission` VALUES ('66', 'Can change user checkout', '22', 'change_usercheckout');
INSERT INTO `auth_permission` VALUES ('67', 'Can delete user checkout', '22', 'delete_usercheckout');
INSERT INTO `auth_permission` VALUES ('68', 'Can add user address', '23', 'add_useraddress');
INSERT INTO `auth_permission` VALUES ('69', 'Can change user address', '23', 'change_useraddress');
INSERT INTO `auth_permission` VALUES ('70', 'Can delete user address', '23', 'delete_useraddress');
INSERT INTO `auth_permission` VALUES ('71', 'Can add order', '24', 'add_order');
INSERT INTO `auth_permission` VALUES ('72', 'Can change order', '24', 'change_order');
INSERT INTO `auth_permission` VALUES ('73', 'Can delete order', '24', 'delete_order');
INSERT INTO `auth_permission` VALUES ('74', 'Can add user profile', '25', 'add_userprofile');
INSERT INTO `auth_permission` VALUES ('75', 'Can change user profile', '25', 'change_userprofile');
INSERT INTO `auth_permission` VALUES ('76', 'Can delete user profile', '25', 'delete_userprofile');
INSERT INTO `auth_permission` VALUES ('77', 'Can add crowdfunding', '26', 'add_crowdfunding');
INSERT INTO `auth_permission` VALUES ('78', 'Can change crowdfunding', '26', 'change_crowdfunding');
INSERT INTO `auth_permission` VALUES ('79', 'Can delete crowdfunding', '26', 'delete_crowdfunding');
INSERT INTO `auth_permission` VALUES ('80', 'Can add office inspection', '27', 'add_officeinspection');
INSERT INTO `auth_permission` VALUES ('81', 'Can change office inspection', '27', 'change_officeinspection');
INSERT INTO `auth_permission` VALUES ('82', 'Can delete office inspection', '27', 'delete_officeinspection');
INSERT INTO `auth_permission` VALUES ('83', 'Can add daily inspection', '28', 'add_dailyinspection');
INSERT INTO `auth_permission` VALUES ('84', 'Can change daily inspection', '28', 'change_dailyinspection');
INSERT INTO `auth_permission` VALUES ('85', 'Can delete daily inspection', '28', 'delete_dailyinspection');
INSERT INTO `auth_permission` VALUES ('86', 'Can add forklift', '29', 'add_forklift');
INSERT INTO `auth_permission` VALUES ('87', 'Can change forklift', '29', 'change_forklift');
INSERT INTO `auth_permission` VALUES ('88', 'Can delete forklift', '29', 'delete_forklift');
INSERT INTO `auth_permission` VALUES ('89', 'Can add forklift_image', '30', 'add_forklift_image');
INSERT INTO `auth_permission` VALUES ('90', 'Can change forklift_image', '30', 'change_forklift_image');
INSERT INTO `auth_permission` VALUES ('91', 'Can delete forklift_image', '30', 'delete_forklift_image');
INSERT INTO `auth_permission` VALUES ('92', 'Can add forklift_maint', '31', 'add_forklift_maint');
INSERT INTO `auth_permission` VALUES ('93', 'Can change forklift_maint', '31', 'change_forklift_maint');
INSERT INTO `auth_permission` VALUES ('94', 'Can delete forklift_maint', '31', 'delete_forklift_maint');
INSERT INTO `auth_permission` VALUES ('95', 'Can add forklift_repair', '32', 'add_forklift_repair');
INSERT INTO `auth_permission` VALUES ('96', 'Can change forklift_repair', '32', 'change_forklift_repair');
INSERT INTO `auth_permission` VALUES ('97', 'Can delete forklift_repair', '32', 'delete_forklift_repair');
INSERT INTO `auth_permission` VALUES ('98', 'Can add forklift_annual_inspection', '33', 'add_forklift_annual_inspection');
INSERT INTO `auth_permission` VALUES ('99', 'Can change forklift_annual_inspection', '33', 'change_forklift_annual_inspection');
INSERT INTO `auth_permission` VALUES ('100', 'Can delete forklift_annual_inspection', '33', 'delete_forklift_annual_inspection');
INSERT INTO `auth_permission` VALUES ('101', 'Can add forklift_annual_inspection_image', '34', 'add_forklift_annual_inspection_image');
INSERT INTO `auth_permission` VALUES ('102', 'Can change forklift_annual_inspection_image', '34', 'change_forklift_annual_inspection_image');
INSERT INTO `auth_permission` VALUES ('103', 'Can delete forklift_annual_inspection_image', '34', 'delete_forklift_annual_inspection_image');
INSERT INTO `auth_permission` VALUES ('104', 'Can add shelf', '35', 'add_shelf');
INSERT INTO `auth_permission` VALUES ('105', 'Can change shelf', '35', 'change_shelf');
INSERT INTO `auth_permission` VALUES ('106', 'Can delete shelf', '35', 'delete_shelf');
INSERT INTO `auth_permission` VALUES ('107', 'Can add shelf_inspection', '36', 'add_shelf_inspection');
INSERT INTO `auth_permission` VALUES ('108', 'Can change shelf_inspection', '36', 'change_shelf_inspection');
INSERT INTO `auth_permission` VALUES ('109', 'Can delete shelf_inspection', '36', 'delete_shelf_inspection');
INSERT INTO `auth_permission` VALUES ('110', 'Can add shelf_inspection_record', '37', 'add_shelf_inspection_record');
INSERT INTO `auth_permission` VALUES ('111', 'Can change shelf_inspection_record', '37', 'change_shelf_inspection_record');
INSERT INTO `auth_permission` VALUES ('112', 'Can delete shelf_inspection_record', '37', 'delete_shelf_inspection_record');
INSERT INTO `auth_permission` VALUES ('113', 'Can add shelf_annual_inspection', '38', 'add_shelf_annual_inspection');
INSERT INTO `auth_permission` VALUES ('114', 'Can change shelf_annual_inspection', '38', 'change_shelf_annual_inspection');
INSERT INTO `auth_permission` VALUES ('115', 'Can delete shelf_annual_inspection', '38', 'delete_shelf_annual_inspection');
INSERT INTO `auth_permission` VALUES ('116', 'Can add shelf_annual_inspection_image', '39', 'add_shelf_annual_inspection_image');
INSERT INTO `auth_permission` VALUES ('117', 'Can change shelf_annual_inspection_image', '39', 'change_shelf_annual_inspection_image');
INSERT INTO `auth_permission` VALUES ('118', 'Can delete shelf_annual_inspection_image', '39', 'delete_shelf_annual_inspection_image');
INSERT INTO `auth_permission` VALUES ('119', 'Can add extinguisher', '40', 'add_extinguisher');
INSERT INTO `auth_permission` VALUES ('120', 'Can change extinguisher', '40', 'change_extinguisher');
INSERT INTO `auth_permission` VALUES ('121', 'Can delete extinguisher', '40', 'delete_extinguisher');
INSERT INTO `auth_permission` VALUES ('122', 'Can add extinguisher_inspection', '41', 'add_extinguisher_inspection');
INSERT INTO `auth_permission` VALUES ('123', 'Can change extinguisher_inspection', '41', 'change_extinguisher_inspection');
INSERT INTO `auth_permission` VALUES ('124', 'Can delete extinguisher_inspection', '41', 'delete_extinguisher_inspection');
INSERT INTO `auth_permission` VALUES ('125', 'Can add hydrant', '42', 'add_hydrant');
INSERT INTO `auth_permission` VALUES ('126', 'Can change hydrant', '42', 'change_hydrant');
INSERT INTO `auth_permission` VALUES ('127', 'Can delete hydrant', '42', 'delete_hydrant');
INSERT INTO `auth_permission` VALUES ('128', 'Can add hydrant_inspection', '43', 'add_hydrant_inspection');
INSERT INTO `auth_permission` VALUES ('129', 'Can change hydrant_inspection', '43', 'change_hydrant_inspection');
INSERT INTO `auth_permission` VALUES ('130', 'Can delete hydrant_inspection', '43', 'delete_hydrant_inspection');
INSERT INTO `auth_permission` VALUES ('131', 'Can add rehearsal', '44', 'add_rehearsal');
INSERT INTO `auth_permission` VALUES ('132', 'Can change rehearsal', '44', 'change_rehearsal');
INSERT INTO `auth_permission` VALUES ('133', 'Can delete rehearsal', '44', 'delete_rehearsal');
INSERT INTO `auth_permission` VALUES ('134', 'Can add registration profile', '45', 'add_registrationprofile');
INSERT INTO `auth_permission` VALUES ('135', 'Can change registration profile', '45', 'change_registrationprofile');
INSERT INTO `auth_permission` VALUES ('136', 'Can delete registration profile', '45', 'delete_registrationprofile');
INSERT INTO `auth_permission` VALUES ('137', 'Can add OTP Token', '46', 'add_phonetoken');
INSERT INTO `auth_permission` VALUES ('138', 'Can change OTP Token', '46', 'change_phonetoken');
INSERT INTO `auth_permission` VALUES ('139', 'Can delete OTP Token', '46', 'delete_phonetoken');

-- ----------------------------
-- Table structure for `authwrapper_myuser`
-- ----------------------------
DROP TABLE IF EXISTS `authwrapper_myuser`;
CREATE TABLE `authwrapper_myuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `sex` varchar(30) NOT NULL,
  `birthday` date DEFAULT NULL,
  `nickname` varchar(30) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  `account_type` varchar(50) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of authwrapper_myuser
-- ----------------------------
INSERT INTO `authwrapper_myuser` VALUES ('1', 'pbkdf2_sha256$20000$xTcBg1XcKR9q$vn4xkcMq5Fya5hetrqSN2bP31r/fyw2Zxt1MwyCEhos=', '2017-09-16 16:00:18', '1', 'bhe001', '+8613500000000', 'Bin', 'He', 'bin.he@live.com', 'male', null, 'hebinn', '1', '1', '2017-07-09 13:19:00', 'phone', '');
INSERT INTO `authwrapper_myuser` VALUES ('42', 'pbkdf2_sha256$20000$LdqcjbJCu1WJ$ZVLHZwvY1/+mZeDp33TkeFKvzfNJW5fmczAXb7wJeiY=', '2017-08-12 05:56:02', '0', '13500000001', '+8613500000001', '', '', null, 'male', null, '', '0', '1', '2017-07-15 05:55:00', 'phone', 'upload\\1-160409144252927.jpg');
INSERT INTO `authwrapper_myuser` VALUES ('43', 'pbkdf2_sha256$20000$aQYAdoWXcyPg$KJIYAKLDa1hPhNgo+1dQ5/MZ3uRaHvnSeXQvc2tD0+I=', '2017-07-16 01:13:22', '0', '13600000000', '+8613600000000', '', '', null, 'male', '2017-07-15', '', '1', '1', '2017-07-15 05:56:00', 'phone', '');
INSERT INTO `authwrapper_myuser` VALUES ('44', 'pbkdf2_sha256$20000$TmRmDeFKp2JM$gRAzEr7qkhkdrIcdYcTisw8ajNbTTtY1FnUysB2Owmo=', null, '0', '+8613700000000', '+8613700000000', '', '', null, 'male', null, '', '0', '0', '2017-07-15 05:58:29', 'phone', '');
INSERT INTO `authwrapper_myuser` VALUES ('45', 'pbkdf2_sha256$20000$etHAFBKua3PB$lIW+BySQssQu6EtOg0ZsljrUhsoJ2EJIoBeiAnDqshk=', '2017-07-15 09:59:37', '0', '+8613900000000', '+8613900000000', '', '', null, 'male', '2017-07-15', '', '0', '1', '2017-07-15 09:59:32', 'phone', '');
INSERT INTO `authwrapper_myuser` VALUES ('46', 'pbkdf2_sha256$20000$93zTmTq4YfKU$+7qsSsjGSJnvn88NoaqAHpQuFTrUWW0ReH49DFT/bUk=', '2017-07-15 10:03:00', '0', '+8613901234567', '+8613901234567', '', '', null, 'male', '2017-07-15', '', '0', '1', '2017-07-15 10:02:40', 'phone', 'profile/+8613901234567/1029263936-0-46.jpg');
INSERT INTO `authwrapper_myuser` VALUES ('47', 'pbkdf2_sha256$20000$xz1RN4Fb7B9k$aiPST3qUdmcANPa1OX3AWVFi+dPaq5Z0S/uoTdTttaA=', null, '1', '+8613800000000', '+8613800000000', '', '', null, 'male', null, '', '1', '1', '2017-08-29 13:58:04', 'phone', '');

-- ----------------------------
-- Table structure for `authwrapper_myuser_groups`
-- ----------------------------
DROP TABLE IF EXISTS `authwrapper_myuser_groups`;
CREATE TABLE `authwrapper_myuser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myuser_id` (`myuser_id`,`group_id`),
  KEY `authwrapper_myuser_groups_group_id_4fd1194d_fk_auth_group_id` (`group_id`),
  CONSTRAINT `authwrapper_myuser_g_myuser_id_673733be_fk_authwrapper_myuser_id` FOREIGN KEY (`myuser_id`) REFERENCES `authwrapper_myuser` (`id`),
  CONSTRAINT `authwrapper_myuser_groups_group_id_4fd1194d_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of authwrapper_myuser_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `authwrapper_myuser_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `authwrapper_myuser_user_permissions`;
CREATE TABLE `authwrapper_myuser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myuser_id` (`myuser_id`,`permission_id`),
  KEY `authwrapper_myuser_u_permission_id_ee6d54e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `authwrapper_myuser_u_myuser_id_2ad23150_fk_authwrapper_myuser_id` FOREIGN KEY (`myuser_id`) REFERENCES `authwrapper_myuser` (`id`),
  CONSTRAINT `authwrapper_myuser_u_permission_id_ee6d54e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of authwrapper_myuser_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `authwrapper_wechatuserprofile`
-- ----------------------------
DROP TABLE IF EXISTS `authwrapper_wechatuserprofile`;
CREATE TABLE `authwrapper_wechatuserprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `openid` varchar(120) DEFAULT NULL,
  `unionid` varchar(120) DEFAULT NULL,
  `privilege` varchar(120) DEFAULT NULL,
  `headimgurl` varchar(500) DEFAULT NULL,
  `nickname` varchar(120) DEFAULT NULL,
  `sex` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `country` varchar(45) DEFAULT NULL,
  `language` varchar(45) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authwrapper_wechatuser_user_id_196b5846_fk_authwrapper_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `authwrapper_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of authwrapper_wechatuserprofile
-- ----------------------------

-- ----------------------------
-- Table structure for `carts_cart`
-- ----------------------------
DROP TABLE IF EXISTS `carts_cart`;
CREATE TABLE `carts_cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` datetime NOT NULL,
  `updated` datetime NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `subtotal` decimal(50,2) NOT NULL,
  `tax_total` decimal(50,2) NOT NULL,
  `total` decimal(50,2) NOT NULL,
  `tax_percentage` decimal(10,5) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `carts_cart_e8701ad4` (`user_id`),
  CONSTRAINT `carts_cart_user_id_4cb3f9df_fk_authwrapper_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `authwrapper_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of carts_cart
-- ----------------------------
INSERT INTO `carts_cart` VALUES ('1', '2017-09-17 08:40:31', '2017-09-17 08:40:31', '1', '25.00', '1.88', '26.88', '0.07500');

-- ----------------------------
-- Table structure for `carts_cartitem`
-- ----------------------------
DROP TABLE IF EXISTS `carts_cartitem`;
CREATE TABLE `carts_cartitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` int(10) unsigned NOT NULL,
  `cart_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `line_item_total` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `carts_cartitem_cart_id_16edfd1_fk_carts_cart_id` (`cart_id`),
  KEY `carts_cartitem_item_id_1b39afc6_fk_products_variation_id` (`item_id`),
  CONSTRAINT `carts_cartitem_cart_id_16edfd1_fk_carts_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `carts_cart` (`id`),
  CONSTRAINT `carts_cartitem_item_id_1b39afc6_fk_products_variation_id` FOREIGN KEY (`item_id`) REFERENCES `products_variation` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of carts_cartitem
-- ----------------------------

-- ----------------------------
-- Table structure for `comments_mpttcomment`
-- ----------------------------
DROP TABLE IF EXISTS `comments_mpttcomment`;
CREATE TABLE `comments_mpttcomment` (
  `comment_ptr_id` int(11) NOT NULL,
  `lft` int(10) unsigned NOT NULL,
  `rght` int(10) unsigned NOT NULL,
  `tree_id` int(10) unsigned NOT NULL,
  `level` int(10) unsigned NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`comment_ptr_id`),
  KEY `comments_mpttcomment_caf7cc51` (`lft`),
  KEY `comments_mpttcomment_3cfbd988` (`rght`),
  KEY `comments_mpttcomment_656442a0` (`tree_id`),
  KEY `comments_mpttcomment_c9e9a848` (`level`),
  KEY `comments_mpttcomment_6be37982` (`parent_id`),
  CONSTRAINT `commen_parent_id_57eaa83b_fk_comments_mpttcomment_comment_ptr_id` FOREIGN KEY (`parent_id`) REFERENCES `comments_mpttcomment` (`comment_ptr_id`),
  CONSTRAINT `comments_mpttcomme_comment_ptr_id_4e1103e4_fk_django_comments_id` FOREIGN KEY (`comment_ptr_id`) REFERENCES `django_comments` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of comments_mpttcomment
-- ----------------------------

-- ----------------------------
-- Table structure for `crowdfundings_crowdfunding`
-- ----------------------------
DROP TABLE IF EXISTS `crowdfundings_crowdfunding`;
CREATE TABLE `crowdfundings_crowdfunding` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(45) NOT NULL,
  `title` varchar(120) NOT NULL,
  `detail` longtext,
  `is_favorite` tinyint(1) NOT NULL,
  `image` varchar(100) NOT NULL,
  `date_joined` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `amount` decimal(50,0) NOT NULL,
  `deadline` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `crowdfundings_crowdfun_user_id_4896770f_fk_authwrapper_myuser_id` (`user_id`),
  CONSTRAINT `crowdfundings_crowdfun_user_id_4896770f_fk_authwrapper_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `authwrapper_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crowdfundings_crowdfunding
-- ----------------------------
INSERT INTO `crowdfundings_crowdfunding` VALUES ('1', 'health', '测试', '测试', '1', 'crowdfunding/bhe001/-None.jpg', '2017-09-17 07:02:00', '1', '100', '2017-09-17 07:02:00');

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_1c5f563_fk_authwrapper_myuser_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_authwrapper_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `authwrapper_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2017-08-29 14:08:54', '1', 'shelf3 1 1 1 1', '1', '', '35', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2017-08-29 14:09:18', '2', 'shelf2 2 2 2 2', '1', '', '35', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2017-08-29 14:09:27', '1', 'shelf inspection 2017-08-29 1', '1', '', '36', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2017-09-16 16:25:34', '1', '日常巡检大', '2', '已修改 impact，image_before 和 image_after 。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2017-09-16 16:27:25', '2', '日常巡检大', '2', '已修改 impact 和 image_before 。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2017-09-17 02:44:46', '8', 'iPhone', '2', '已修改 image 。', '19', '1');

-- ----------------------------
-- Table structure for `django_comment_flags`
-- ----------------------------
DROP TABLE IF EXISTS `django_comment_flags`;
CREATE TABLE `django_comment_flags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `flag` varchar(30) NOT NULL,
  `flag_date` datetime NOT NULL,
  `comment_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_comment_flags_user_id_641f11c1_uniq` (`user_id`,`comment_id`,`flag`),
  KEY `django_comment_flags_comment_id_7f2b4c55_fk_django_comments_id` (`comment_id`),
  KEY `django_comment_flags_327a6c43` (`flag`),
  CONSTRAINT `django_comment_flags_comment_id_7f2b4c55_fk_django_comments_id` FOREIGN KEY (`comment_id`) REFERENCES `django_comments` (`id`),
  CONSTRAINT `django_comment_flags_user_id_3512f4c_fk_authwrapper_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `authwrapper_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_comment_flags
-- ----------------------------

-- ----------------------------
-- Table structure for `django_comments`
-- ----------------------------
DROP TABLE IF EXISTS `django_comments`;
CREATE TABLE `django_comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `object_pk` longtext NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_email` varchar(254) NOT NULL,
  `user_url` varchar(200) NOT NULL,
  `comment` longtext NOT NULL,
  `submit_date` datetime NOT NULL,
  `ip_address` char(39) DEFAULT NULL,
  `is_public` tinyint(1) NOT NULL,
  `is_removed` tinyint(1) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `django_commen_content_type_id_5626a505_fk_django_content_type_id` (`content_type_id`),
  KEY `django_comments_site_id_6ea83216_fk_django_site_id` (`site_id`),
  KEY `django_comments_user_id_2c584e2_fk_authwrapper_myuser_id` (`user_id`),
  KEY `django_comments_submit_date_5c84a37e_uniq` (`submit_date`),
  CONSTRAINT `django_commen_content_type_id_5626a505_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_comments_site_id_6ea83216_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`),
  CONSTRAINT `django_comments_user_id_2c584e2_fk_authwrapper_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `authwrapper_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_comments
-- ----------------------------

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('9', 'authwrapper', 'myuser');
INSERT INTO `django_content_type` VALUES ('10', 'authwrapper', 'wechatuserprofile');
INSERT INTO `django_content_type` VALUES ('21', 'carts', 'cart');
INSERT INTO `django_content_type` VALUES ('20', 'carts', 'cartitem');
INSERT INTO `django_content_type` VALUES ('11', 'comments', 'mpttcomment');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('26', 'crowdfundings', 'crowdfunding');
INSERT INTO `django_content_type` VALUES ('7', 'django_comments', 'comment');
INSERT INTO `django_content_type` VALUES ('8', 'django_comments', 'commentflag');
INSERT INTO `django_content_type` VALUES ('28', 'inspection', 'dailyinspection');
INSERT INTO `django_content_type` VALUES ('40', 'inspection', 'extinguisher');
INSERT INTO `django_content_type` VALUES ('41', 'inspection', 'extinguisher_inspection');
INSERT INTO `django_content_type` VALUES ('29', 'inspection', 'forklift');
INSERT INTO `django_content_type` VALUES ('33', 'inspection', 'forklift_annual_inspection');
INSERT INTO `django_content_type` VALUES ('34', 'inspection', 'forklift_annual_inspection_image');
INSERT INTO `django_content_type` VALUES ('30', 'inspection', 'forklift_image');
INSERT INTO `django_content_type` VALUES ('31', 'inspection', 'forklift_maint');
INSERT INTO `django_content_type` VALUES ('32', 'inspection', 'forklift_repair');
INSERT INTO `django_content_type` VALUES ('42', 'inspection', 'hydrant');
INSERT INTO `django_content_type` VALUES ('43', 'inspection', 'hydrant_inspection');
INSERT INTO `django_content_type` VALUES ('27', 'inspection', 'officeinspection');
INSERT INTO `django_content_type` VALUES ('44', 'inspection', 'rehearsal');
INSERT INTO `django_content_type` VALUES ('35', 'inspection', 'shelf');
INSERT INTO `django_content_type` VALUES ('38', 'inspection', 'shelf_annual_inspection');
INSERT INTO `django_content_type` VALUES ('39', 'inspection', 'shelf_annual_inspection_image');
INSERT INTO `django_content_type` VALUES ('36', 'inspection', 'shelf_inspection');
INSERT INTO `django_content_type` VALUES ('37', 'inspection', 'shelf_inspection_record');
INSERT INTO `django_content_type` VALUES ('14', 'newsletter', 'article');
INSERT INTO `django_content_type` VALUES ('13', 'newsletter', 'banner');
INSERT INTO `django_content_type` VALUES ('12', 'newsletter', 'signup');
INSERT INTO `django_content_type` VALUES ('24', 'orders', 'order');
INSERT INTO `django_content_type` VALUES ('23', 'orders', 'useraddress');
INSERT INTO `django_content_type` VALUES ('22', 'orders', 'usercheckout');
INSERT INTO `django_content_type` VALUES ('25', 'personalcenter', 'userprofile');
INSERT INTO `django_content_type` VALUES ('46', 'phone_login', 'phonetoken');
INSERT INTO `django_content_type` VALUES ('18', 'products', 'category');
INSERT INTO `django_content_type` VALUES ('15', 'products', 'product');
INSERT INTO `django_content_type` VALUES ('19', 'products', 'productfeatured');
INSERT INTO `django_content_type` VALUES ('17', 'products', 'productimage');
INSERT INTO `django_content_type` VALUES ('16', 'products', 'variation');
INSERT INTO `django_content_type` VALUES ('45', 'registration', 'registrationprofile');
INSERT INTO `django_content_type` VALUES ('5', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('6', 'sites', 'site');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2017-08-28 15:03:09');
INSERT INTO `django_migrations` VALUES ('2', 'contenttypes', '0002_remove_content_type_name', '2017-08-28 15:03:10');
INSERT INTO `django_migrations` VALUES ('3', 'auth', '0001_initial', '2017-08-28 15:03:10');
INSERT INTO `django_migrations` VALUES ('4', 'auth', '0002_alter_permission_name_max_length', '2017-08-28 15:03:11');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0003_alter_user_email_max_length', '2017-08-28 15:03:11');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0004_alter_user_username_opts', '2017-08-28 15:03:11');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0005_alter_user_last_login_null', '2017-08-28 15:03:11');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0006_require_contenttypes_0002', '2017-08-28 15:03:11');
INSERT INTO `django_migrations` VALUES ('9', 'authwrapper', '0001_initial', '2017-08-28 15:03:12');
INSERT INTO `django_migrations` VALUES ('10', 'admin', '0001_initial', '2017-08-28 15:03:12');
INSERT INTO `django_migrations` VALUES ('11', 'authwrapper', '0002_wechatuserprofile', '2017-08-28 15:03:12');
INSERT INTO `django_migrations` VALUES ('12', 'authwrapper', '0003_auto_20170710_0758', '2017-08-28 15:03:13');
INSERT INTO `django_migrations` VALUES ('13', 'products', '0001_initial', '2017-08-28 15:03:13');
INSERT INTO `django_migrations` VALUES ('14', 'products', '0002_variation', '2017-08-28 15:03:13');
INSERT INTO `django_migrations` VALUES ('15', 'products', '0003_productimage', '2017-08-28 15:03:13');
INSERT INTO `django_migrations` VALUES ('16', 'products', '0004_auto_20160927_0832', '2017-08-28 15:03:14');
INSERT INTO `django_migrations` VALUES ('17', 'products', '0005_auto_20161002_1626', '2017-08-28 15:03:14');
INSERT INTO `django_migrations` VALUES ('18', 'products', '0006_productfeatured', '2017-08-28 15:03:14');
INSERT INTO `django_migrations` VALUES ('19', 'carts', '0001_initial', '2017-08-28 15:03:15');
INSERT INTO `django_migrations` VALUES ('20', 'carts', '0002_cartitem_line_item_total', '2017-08-28 15:03:15');
INSERT INTO `django_migrations` VALUES ('21', 'carts', '0003_cart_subtotal', '2017-08-28 15:03:16');
INSERT INTO `django_migrations` VALUES ('22', 'carts', '0004_auto_20161007_1052', '2017-08-28 15:03:16');
INSERT INTO `django_migrations` VALUES ('23', 'carts', '0005_cart_tax_percentage', '2017-08-28 15:03:17');
INSERT INTO `django_migrations` VALUES ('24', 'sites', '0001_initial', '2017-08-28 15:03:17');
INSERT INTO `django_migrations` VALUES ('25', 'django_comments', '0001_initial', '2017-08-28 15:03:18');
INSERT INTO `django_migrations` VALUES ('26', 'django_comments', '0002_update_user_email_field_length', '2017-08-28 15:03:18');
INSERT INTO `django_migrations` VALUES ('27', 'django_comments', '0003_add_submit_date_index', '2017-08-28 15:03:18');
INSERT INTO `django_migrations` VALUES ('28', 'comments', '0001_initial', '2017-08-28 15:03:19');
INSERT INTO `django_migrations` VALUES ('29', 'crowdfundings', '0001_initial', '2017-08-28 15:03:19');
INSERT INTO `django_migrations` VALUES ('30', 'crowdfundings', '0002_auto_20161224_1500', '2017-08-28 15:03:20');
INSERT INTO `django_migrations` VALUES ('31', 'inspection', '0001_initial', '2017-08-28 15:03:20');
INSERT INTO `django_migrations` VALUES ('32', 'inspection', '0002_officeinspection_comments', '2017-08-28 15:03:20');
INSERT INTO `django_migrations` VALUES ('33', 'inspection', '0003_officeinspection_power', '2017-08-28 15:03:20');
INSERT INTO `django_migrations` VALUES ('34', 'inspection', '0004_auto_20170810_2341', '2017-08-28 15:03:21');
INSERT INTO `django_migrations` VALUES ('35', 'inspection', '0005_officeinspection_image', '2017-08-28 15:03:21');
INSERT INTO `django_migrations` VALUES ('36', 'inspection', '0006_dailyinspection', '2017-08-28 15:03:21');
INSERT INTO `django_migrations` VALUES ('37', 'inspection', '0007_dailyinspection_due_date', '2017-08-28 15:03:21');
INSERT INTO `django_migrations` VALUES ('38', 'inspection', '0008_auto_20170824_2041', '2017-08-28 15:03:22');
INSERT INTO `django_migrations` VALUES ('39', 'inspection', '0009_auto_20170826_1415', '2017-08-28 15:03:23');
INSERT INTO `django_migrations` VALUES ('40', 'inspection', '0010_auto_20170826_1438', '2017-08-28 15:03:24');
INSERT INTO `django_migrations` VALUES ('41', 'inspection', '0011_auto_20170826_1528', '2017-08-28 15:03:25');
INSERT INTO `django_migrations` VALUES ('42', 'inspection', '0012_extinguisher_inspection_hydrant_inspection', '2017-08-28 15:03:25');
INSERT INTO `django_migrations` VALUES ('43', 'inspection', '0013_auto_20170827_2203', '2017-08-28 15:03:25');
INSERT INTO `django_migrations` VALUES ('44', 'inspection', '0014_delete_shelf_inspection', '2017-08-28 15:03:26');
INSERT INTO `django_migrations` VALUES ('45', 'inspection', '0015_auto_20170828_0819', '2017-08-28 15:03:26');
INSERT INTO `django_migrations` VALUES ('46', 'inspection', '0016_auto_20170828_1330', '2017-08-28 15:03:27');
INSERT INTO `django_migrations` VALUES ('47', 'inspection', '0017_shelf_inspection_record_forecast_complete_time', '2017-08-28 15:03:27');
INSERT INTO `django_migrations` VALUES ('48', 'inspection', '0018_auto_20170828_1336', '2017-08-28 15:03:27');
INSERT INTO `django_migrations` VALUES ('49', 'newsletter', '0001_initial', '2017-08-28 15:03:28');
INSERT INTO `django_migrations` VALUES ('50', 'newsletter', '0002_userwechat', '2017-08-28 15:03:28');
INSERT INTO `django_migrations` VALUES ('51', 'newsletter', '0003_banner', '2017-08-28 15:03:28');
INSERT INTO `django_migrations` VALUES ('52', 'newsletter', '0004_article', '2017-08-28 15:03:28');
INSERT INTO `django_migrations` VALUES ('53', 'newsletter', '0005_auto_20170624_1138', '2017-08-28 15:03:28');
INSERT INTO `django_migrations` VALUES ('54', 'newsletter', '0006_delete_userwechat', '2017-08-28 15:03:29');
INSERT INTO `django_migrations` VALUES ('55', 'orders', '0001_initial', '2017-08-28 15:03:29');
INSERT INTO `django_migrations` VALUES ('56', 'orders', '0002_useraddress', '2017-08-28 15:03:29');
INSERT INTO `django_migrations` VALUES ('57', 'orders', '0003_order', '2017-08-28 15:03:30');
INSERT INTO `django_migrations` VALUES ('58', 'orders', '0004_order_status', '2017-08-28 15:03:30');
INSERT INTO `django_migrations` VALUES ('59', 'orders', '0005_auto_20161022_1051', '2017-08-28 15:03:31');
INSERT INTO `django_migrations` VALUES ('60', 'orders', '0006_auto_20170326_2210', '2017-08-28 15:03:31');
INSERT INTO `django_migrations` VALUES ('61', 'registration', '0001_initial', '2017-08-28 15:03:32');
INSERT INTO `django_migrations` VALUES ('62', 'registration', '0002_registrationprofile_activated', '2017-08-28 15:03:32');
INSERT INTO `django_migrations` VALUES ('63', 'registration', '0003_migrate_activatedstatus', '2017-08-28 15:03:32');
INSERT INTO `django_migrations` VALUES ('64', 'sessions', '0001_initial', '2017-08-28 15:03:33');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('15jd52e6uuty94nrdt8484fd5uztvxnu', 'NzQ2ZjhlMDZlNTBlODFmY2YzYjljNzBlZWEwNDczODEzZWYyMTcwYTp7Il9hdXRoX3VzZXJfaGFzaCI6IjVmNzY3NjE0NDg3NWUzNjU1ZGU5MmRjNmRhODY2NTUyM2I2YmRjYzEiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImF1dGh3cmFwcGVyLmJhY2tlbmRzLmF1dGguTXlCYWNrZW5kIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-10-01 23:23:29');
INSERT INTO `django_session` VALUES ('1ckd580npxujsc9tjylfcevk6xy2x8bk', 'NzcwNjM0NmFiZjc1YjQxZmI4NGQ3MTY2MGZkYmNkNTE5YjgwMGQ3YTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYXV0aHdyYXBwZXIuYmFja2VuZHMuYXV0aC5NeUJhY2tlbmQiLCJfc2Vzc2lvbl9leHBpcnkiOjAsImNhcnRfaXRlbV9jb3VudCI6MCwiX2F1dGhfdXNlcl9oYXNoIjoiNWY3Njc2MTQ0ODc1ZTM2NTVkZTkyZGM2ZGE4NjY1NTIzYjZiZGNjMSIsImNhcnRfaWQiOjF9', '2017-10-02 13:10:38');
INSERT INTO `django_session` VALUES ('azindq6fk2lc1b6zr1tu5fwhdx95hk6i', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-10-01 01:55:17');
INSERT INTO `django_session` VALUES ('dfzs12y8layaqv7xw848wsoz8jsjorhj', 'NzQ2ZjhlMDZlNTBlODFmY2YzYjljNzBlZWEwNDczODEzZWYyMTcwYTp7Il9hdXRoX3VzZXJfaGFzaCI6IjVmNzY3NjE0NDg3NWUzNjU1ZGU5MmRjNmRhODY2NTUyM2I2YmRjYzEiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImF1dGh3cmFwcGVyLmJhY2tlbmRzLmF1dGguTXlCYWNrZW5kIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-10-02 15:42:19');
INSERT INTO `django_session` VALUES ('djppju1u17zbd3v6cpl9fnxeu9d7gi68', 'NzQ2ZjhlMDZlNTBlODFmY2YzYjljNzBlZWEwNDczODEzZWYyMTcwYTp7Il9hdXRoX3VzZXJfaGFzaCI6IjVmNzY3NjE0NDg3NWUzNjU1ZGU5MmRjNmRhODY2NTUyM2I2YmRjYzEiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImF1dGh3cmFwcGVyLmJhY2tlbmRzLmF1dGguTXlCYWNrZW5kIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-10-01 02:44:52');
INSERT INTO `django_session` VALUES ('vngztl6f5nxadmpmqkw1w6w8zbq8wdqx', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-10-01 02:30:26');
INSERT INTO `django_session` VALUES ('wtnmm27vezeivm7869d63prj4p90v9du', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-09-18 14:57:00');

-- ----------------------------
-- Table structure for `django_site`
-- ----------------------------
DROP TABLE IF EXISTS `django_site`;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_site
-- ----------------------------
INSERT INTO `django_site` VALUES ('1', 'example.com', 'example.com');

-- ----------------------------
-- Table structure for `inspection_dailyinspection`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_dailyinspection`;
CREATE TABLE `inspection_dailyinspection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `impact` varchar(30) NOT NULL,
  `owner` varchar(30) NOT NULL,
  `image_before` varchar(100) DEFAULT NULL,
  `image_after` varchar(100) DEFAULT NULL,
  `due_date` date NOT NULL,
  `category` varchar(30) NOT NULL,
  `created` datetime NOT NULL,
  `inspection_content` varchar(30) NOT NULL,
  `location` varchar(30) NOT NULL,
  `rectification_measures` longtext NOT NULL,
  `rectification_status` varchar(30) NOT NULL,
  `updated` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_dailyinspection
-- ----------------------------
INSERT INTO `inspection_dailyinspection` VALUES ('1', '[u\'1\', u\'3\']', '杨志想', 'dailyinspection/machine/20170829003634-20170813_142510.jpg', 'dailyinspection/machine/20170829003634-20170813_145439.jpg', '2017-01-01', 'method', '2017-08-29 00:36:34', '5K33L1纸箱漏油', '1', '立即要求相关人员进行整改', 'completed', '2017-09-17 13:32:34');
INSERT INTO `inspection_dailyinspection` VALUES ('2', '[u\'1\']', '严鹰超', 'dailyinspection/people/2017-09-01-10-57-57-automotive.jpg', '', '2017-08-12', 'people', '2017-09-01 10:57:57', 'X3-106前面放货', '1', '立即要求相关人员进行整改', 'completed', '2017-09-17 13:33:20');
INSERT INTO `inspection_dailyinspection` VALUES ('3', '[u\'1\', u\'3\']', '杨志想', 'dailyinspection/environment/20170917133137-automotive.jpg', '', '2017-08-01', 'environment', '2017-09-17 13:31:37', '52K14散拍未并拍', '1', '立即要求相关人员进行整改', 'completed', '2017-09-17 13:31:37');
INSERT INTO `inspection_dailyinspection` VALUES ('4', '[u\'3\']', '严鹰超', 'dailyinspection/people/20170917133417-projects-and-energy.jpg', '', '2017-08-14', 'people', '2017-09-17 13:34:17', '清洁工具摆放处有大量水渍', '1', '立即要求相关人员进行整改', 'completed', '2017-09-17 13:34:17');
INSERT INTO `inspection_dailyinspection` VALUES ('5', '[u\'1\', u\'3\']', '杨志想', 'dailyinspection/device/20170917133517-projects-and-energy.jpg', '', '2017-08-21', 'device', '2017-09-17 13:35:17', '4号液压车损坏', '1', '立即要求相关人员进行整改', 'completed', '2017-09-17 13:35:17');
INSERT INTO `inspection_dailyinspection` VALUES ('6', '[u\'3\']', '严鹰超', 'dailyinspection/environment/20170917133610-automotive.jpg', '', '2017-09-20', 'environment', '2017-09-17 13:36:10', '5号液压车使用完毕没有及时归位', '1', '立即要求相关人员进行整改', 'uncompleted', '2017-09-18 00:47:41');
INSERT INTO `inspection_dailyinspection` VALUES ('7', '[u\'1\', u\'3\']', '杨志想', 'dailyinspection/people/20170917133700-chemicals.jpg', '', '2017-08-14', 'people', '2017-09-17 13:37:00', '33J5K库边漏雨', '1', '立即要求相关人员进行整改', 'completed', '2017-09-17 13:37:00');
INSERT INTO `inspection_dailyinspection` VALUES ('8', '[u\'1\', u\'3\']', '杨志想', 'dailyinspection/environment/20170917133755-1502042224227609564.jpg', '', '2017-08-14', 'environment', '2017-09-17 13:37:55', '叉车停在人行道上，存在安全隐患', '1', '立即要求相关人员进行整改', 'uncompleted', '2017-09-17 13:52:48');
INSERT INTO `inspection_dailyinspection` VALUES ('9', '[u\'1\', u\'3\']', '严鹰超', 'dailyinspection/device/20170917133842-1502042205287071814.jpg', '', '2017-08-21', 'device', '2017-09-17 13:38:42', '仓库多处使用坏木拍', '1', '立即要求', 'completed', '2017-09-17 13:38:42');

-- ----------------------------
-- Table structure for `inspection_extinguisher`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_extinguisher`;
CREATE TABLE `inspection_extinguisher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `capacity` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_extinguisher
-- ----------------------------

-- ----------------------------
-- Table structure for `inspection_extinguisher_inspection`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_extinguisher_inspection`;
CREATE TABLE `inspection_extinguisher_inspection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `check_person` varchar(30) NOT NULL,
  `check_result` varchar(30) NOT NULL,
  `check_date` date NOT NULL,
  `extinguisher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `inspectio_extinguisher_id_5af9f128_fk_inspection_extinguisher_id` (`extinguisher_id`),
  CONSTRAINT `inspectio_extinguisher_id_5af9f128_fk_inspection_extinguisher_id` FOREIGN KEY (`extinguisher_id`) REFERENCES `inspection_extinguisher` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_extinguisher_inspection
-- ----------------------------

-- ----------------------------
-- Table structure for `inspection_forklift`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_forklift`;
CREATE TABLE `inspection_forklift` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `internal_car_number` varchar(30) NOT NULL,
  `internal_plate_number` varchar(30) NOT NULL,
  `model` varchar(30) NOT NULL,
  `sn` varchar(30) NOT NULL,
  `category` varchar(30) NOT NULL,
  `manufacturer` varchar(30) NOT NULL,
  `tip_height` varchar(30) NOT NULL,
  `carrying_capacity` varchar(30) NOT NULL,
  `self_weight` varchar(30) NOT NULL,
  `turning_radius` varchar(30) NOT NULL,
  `front_tyre_size` varchar(30) NOT NULL,
  `back_tyre_size` varchar(30) NOT NULL,
  `width` varchar(30) NOT NULL,
  `length` varchar(30) NOT NULL,
  `fork_length` varchar(30) NOT NULL,
  `maximum_velocity` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_forklift
-- ----------------------------

-- ----------------------------
-- Table structure for `inspection_forklift_annual_inspection`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_forklift_annual_inspection`;
CREATE TABLE `inspection_forklift_annual_inspection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `next_date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_forklift_annual_inspection
-- ----------------------------

-- ----------------------------
-- Table structure for `inspection_forklift_annual_inspection_image`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_forklift_annual_inspection_image`;
CREATE TABLE `inspection_forklift_annual_inspection_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `forklift_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `D74adfb14db8564695ede5885030f327` (`forklift_id`),
  CONSTRAINT `D74adfb14db8564695ede5885030f327` FOREIGN KEY (`forklift_id`) REFERENCES `inspection_forklift_annual_inspection` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_forklift_annual_inspection_image
-- ----------------------------

-- ----------------------------
-- Table structure for `inspection_forklift_image`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_forklift_image`;
CREATE TABLE `inspection_forklift_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `forklift_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `inspection_forkli_forklift_id_571a9e3c_fk_inspection_forklift_id` (`forklift_id`),
  CONSTRAINT `inspection_forkli_forklift_id_571a9e3c_fk_inspection_forklift_id` FOREIGN KEY (`forklift_id`) REFERENCES `inspection_forklift` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_forklift_image
-- ----------------------------

-- ----------------------------
-- Table structure for `inspection_forklift_maint`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_forklift_maint`;
CREATE TABLE `inspection_forklift_maint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clean_forklift` varchar(30) NOT NULL,
  `clean_and_lubricate_chain` varchar(30) NOT NULL,
  `lubricate_gateshelf_and_lean_cylinder_bearing` varchar(30) NOT NULL,
  `lubricate_sideswayfork_and_check_work_status` varchar(30) NOT NULL,
  `fastening_tyre_nut` varchar(30) NOT NULL,
  `check_tyre_status` varchar(30) NOT NULL,
  `check_gear_oil_level_and_leak` varchar(30) NOT NULL,
  `check_hydraulic_oil_level` varchar(30) NOT NULL,
  `clean_all_motor_and_accessories` varchar(30) NOT NULL,
  `check_and_clean_motor_cooling_fan` varchar(30) NOT NULL,
  `check_all_cable_and_connection_status` varchar(30) NOT NULL,
  `check_battery_electrolyte_liquidometer_ratio` varchar(30) NOT NULL,
  `check_charger_status` varchar(30) NOT NULL,
  `check_pipeline_fastening_and_leak` varchar(30) NOT NULL,
  `check_pallet_fork_and_pin_lock` varchar(30) NOT NULL,
  `check_lubricate_pedal_and_control_linkage` varchar(30) NOT NULL,
  `check_braking_device` varchar(30) NOT NULL,
  `check_all_motor_carbon_brush` varchar(30) NOT NULL,
  `check_overhead_guard_and_counter_weight` varchar(30) NOT NULL,
  `check_steering_axle_and_drive_axle` varchar(30) NOT NULL,
  `check_gateshelf_and_chain` varchar(30) NOT NULL,
  `check_hub_bearing` varchar(30) NOT NULL,
  `check_steering_axle_bearing` varchar(30) NOT NULL,
  `check_gateshlf_bearing` varchar(30) NOT NULL,
  `change_gear_oil` varchar(30) NOT NULL,
  `change_oil_suction_filter` varchar(30) NOT NULL,
  `change_ventilate_filter` varchar(30) NOT NULL,
  `change_hydraulic_oil` varchar(30) NOT NULL,
  `created` datetime NOT NULL,
  `updated` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_forklift_maint
-- ----------------------------

-- ----------------------------
-- Table structure for `inspection_forklift_repair`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_forklift_repair`;
CREATE TABLE `inspection_forklift_repair` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `damage_reason` varchar(30) NOT NULL,
  `accessories_name` varchar(30) NOT NULL,
  `accessories_num` decimal(20,0) NOT NULL,
  `description` longtext NOT NULL,
  `repaired` varchar(30) NOT NULL,
  `created` datetime NOT NULL,
  `updated` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_forklift_repair
-- ----------------------------

-- ----------------------------
-- Table structure for `inspection_hydrant`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_hydrant`;
CREATE TABLE `inspection_hydrant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `accessories` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_hydrant
-- ----------------------------

-- ----------------------------
-- Table structure for `inspection_hydrant_inspection`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_hydrant_inspection`;
CREATE TABLE `inspection_hydrant_inspection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `check_person` varchar(30) NOT NULL,
  `check_result` varchar(30) NOT NULL,
  `check_date` date NOT NULL,
  `extinguisher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `inspection_hydr_extinguisher_id_c60a0d0_fk_inspection_hydrant_id` (`extinguisher_id`),
  CONSTRAINT `inspection_hydr_extinguisher_id_c60a0d0_fk_inspection_hydrant_id` FOREIGN KEY (`extinguisher_id`) REFERENCES `inspection_hydrant` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_hydrant_inspection
-- ----------------------------

-- ----------------------------
-- Table structure for `inspection_officeinspection`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_officeinspection`;
CREATE TABLE `inspection_officeinspection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `plug` varchar(30) NOT NULL,
  `location` varchar(120) DEFAULT NULL,
  `timestamp` datetime NOT NULL,
  `updated` datetime NOT NULL,
  `comments` longtext,
  `power` varchar(30) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_officeinspection
-- ----------------------------

-- ----------------------------
-- Table structure for `inspection_rehearsal`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_rehearsal`;
CREATE TABLE `inspection_rehearsal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` longtext NOT NULL,
  `date` date NOT NULL,
  `attachment` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_rehearsal
-- ----------------------------

-- ----------------------------
-- Table structure for `inspection_shelf`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_shelf`;
CREATE TABLE `inspection_shelf` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(30) NOT NULL,
  `warehouse` varchar(30) NOT NULL,
  `compartment` varchar(30) NOT NULL,
  `warehouse_channel` varchar(30) NOT NULL,
  `group` varchar(30) NOT NULL,
  `number` varchar(30) NOT NULL,
  `is_gradient_measurement_mandatory` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_shelf
-- ----------------------------
INSERT INTO `inspection_shelf` VALUES ('1', '横梁式', '3', '1', '1', '1', '1', '0');
INSERT INTO `inspection_shelf` VALUES ('2', '横梁式', '2', '2', '2', '2', '2', '0');

-- ----------------------------
-- Table structure for `inspection_shelf_annual_inspection`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_shelf_annual_inspection`;
CREATE TABLE `inspection_shelf_annual_inspection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `next_date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_shelf_annual_inspection
-- ----------------------------

-- ----------------------------
-- Table structure for `inspection_shelf_annual_inspection_image`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_shelf_annual_inspection_image`;
CREATE TABLE `inspection_shelf_annual_inspection_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `shelf_annual_inspection_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `D09124180f0a38147d5b9c6a147d5259` (`shelf_annual_inspection_id`),
  CONSTRAINT `D09124180f0a38147d5b9c6a147d5259` FOREIGN KEY (`shelf_annual_inspection_id`) REFERENCES `inspection_shelf_annual_inspection` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_shelf_annual_inspection_image
-- ----------------------------

-- ----------------------------
-- Table structure for `inspection_shelf_inspection`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_shelf_inspection`;
CREATE TABLE `inspection_shelf_inspection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `check_date` date NOT NULL,
  `comments` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_shelf_inspection
-- ----------------------------
INSERT INTO `inspection_shelf_inspection` VALUES ('1', '2017-08-29', '');

-- ----------------------------
-- Table structure for `inspection_shelf_inspection_record`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_shelf_inspection_record`;
CREATE TABLE `inspection_shelf_inspection_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `use_condition` varchar(30) NOT NULL,
  `is_locked` tinyint(1) NOT NULL,
  `check_person` varchar(30) NOT NULL,
  `gradient` decimal(20,1) DEFAULT NULL,
  `comments` longtext,
  `shelf_id` int(11) NOT NULL,
  `shelf_inspection_id` int(11) NOT NULL,
  `forecast_complete_time` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `inspection_shelf_inspec_shelf_id_175de8b1_fk_inspection_shelf_id` (`shelf_id`),
  KEY `inspection_shelf_inspection_record_8b1352f8` (`shelf_inspection_id`),
  CONSTRAINT `i_shelf_inspection_id_4fdf5361_fk_inspection_shelf_inspection_id` FOREIGN KEY (`shelf_inspection_id`) REFERENCES `inspection_shelf_inspection` (`id`),
  CONSTRAINT `inspection_shelf_inspec_shelf_id_175de8b1_fk_inspection_shelf_id` FOREIGN KEY (`shelf_id`) REFERENCES `inspection_shelf` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_shelf_inspection_record
-- ----------------------------
INSERT INTO `inspection_shelf_inspection_record` VALUES ('1', '1', '1', '张三', '11.0', '', '1', '1', '2017-08-29');
INSERT INTO `inspection_shelf_inspection_record` VALUES ('2', '2', '0', '发放', '0.5', '', '2', '1', '2017-08-29');

-- ----------------------------
-- Table structure for `newsletter_article`
-- ----------------------------
DROP TABLE IF EXISTS `newsletter_article`;
CREATE TABLE `newsletter_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(150) NOT NULL,
  `content` longtext NOT NULL,
  `publishtime` datetime NOT NULL,
  `abstract` longtext NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of newsletter_article
-- ----------------------------
INSERT INTO `newsletter_article` VALUES ('1', '119th Spring Canton Fair', '<h2><img alt=\"\" src=\"http://www.cofoe.com/uploads/allimg/160507/1-16050G4095T94.jpg\" style=\"height:371px; width:500px\" /></h2>\r\n\r\n<h2>119th Spring <strong>Canton</strong> Fair</h2>\r\n\r\n<p>成功</p>\r\n\r\n<p>&nbsp;</p>\r\n', '2017-04-30 04:47:01', '119th Spring Canton Fair', 'article/119th-spring-canton-fair.jpg');
INSERT INTO `newsletter_article` VALUES ('2', 'The 118th China Import and Export Fair in Guangzhou', '<p><img alt=\"\" src=\"http://www.cofoe.com/uploads/allimg/151208/1-15120Q61405418.png\" style=\"height:364px; width:489px\" /></p>\r\n', '2017-04-30 05:51:19', ' Hunan KeYuan Medical Equipment Co.,Ltd. attend the 118th China Import and Export Fair in Guangzhou \r\n', 'article/the-118th-china-import-and-export-fair-in-guangzhou_0UMEcHn.jpg');
INSERT INTO `newsletter_article` VALUES ('3', '2016 CMEF in Shanghai', '<p><img alt=\"\" src=\"http://www.cofoe.com/uploads/allimg/160428/1-16042Q12154460.jpg\" style=\"height:500px; width:674px\" /></p>\r\n', '2017-04-30 07:23:09', 'Hunan Cofoe Medical Technology Development Co.,Ltd. attend 2016 CMEF in Shanghai ', 'article/2016-cmef-in-shanghai.jpg');

-- ----------------------------
-- Table structure for `newsletter_banner`
-- ----------------------------
DROP TABLE IF EXISTS `newsletter_banner`;
CREATE TABLE `newsletter_banner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `title` varchar(120) DEFAULT NULL,
  `text` varchar(220) DEFAULT NULL,
  `active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of newsletter_banner
-- ----------------------------
INSERT INTO `newsletter_banner` VALUES ('1', 'banner/banner1.png', 'banner1', 'banner1', '1');
INSERT INTO `newsletter_banner` VALUES ('2', 'banner/banner2.png', 'banner2', 'banner2', '1');
INSERT INTO `newsletter_banner` VALUES ('3', 'banner/banner3.png', 'banner3', 'banner3', '1');

-- ----------------------------
-- Table structure for `newsletter_signup`
-- ----------------------------
DROP TABLE IF EXISTS `newsletter_signup`;
CREATE TABLE `newsletter_signup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `full_name` varchar(120) DEFAULT NULL,
  `timestamp` datetime NOT NULL,
  `updated` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of newsletter_signup
-- ----------------------------

-- ----------------------------
-- Table structure for `orders_order`
-- ----------------------------
DROP TABLE IF EXISTS `orders_order`;
CREATE TABLE `orders_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shipping_total_price` decimal(50,2) NOT NULL,
  `order_total` decimal(50,2) NOT NULL,
  `billing_address_id` int(11) DEFAULT NULL,
  `cart_id` int(11) NOT NULL,
  `shipping_address_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `status` varchar(120) NOT NULL,
  `order_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_orde_billing_address_id_5afecadd_fk_orders_useraddress_id` (`billing_address_id`),
  KEY `orders_order_cart_id_2f8c40e6_fk_carts_cart_id` (`cart_id`),
  KEY `orders_ord_shipping_address_id_491fafef_fk_orders_useraddress_id` (`shipping_address_id`),
  KEY `orders_order_user_id_5bd989c5_fk_orders_usercheckout_id` (`user_id`),
  CONSTRAINT `orders_ord_shipping_address_id_491fafef_fk_orders_useraddress_id` FOREIGN KEY (`shipping_address_id`) REFERENCES `orders_useraddress` (`id`),
  CONSTRAINT `orders_orde_billing_address_id_5afecadd_fk_orders_useraddress_id` FOREIGN KEY (`billing_address_id`) REFERENCES `orders_useraddress` (`id`),
  CONSTRAINT `orders_order_cart_id_2f8c40e6_fk_carts_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `carts_cart` (`id`),
  CONSTRAINT `orders_order_user_id_5bd989c5_fk_orders_usercheckout_id` FOREIGN KEY (`user_id`) REFERENCES `orders_usercheckout` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of orders_order
-- ----------------------------

-- ----------------------------
-- Table structure for `orders_useraddress`
-- ----------------------------
DROP TABLE IF EXISTS `orders_useraddress`;
CREATE TABLE `orders_useraddress` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(120) NOT NULL,
  `street` varchar(120) NOT NULL,
  `city` varchar(120) NOT NULL,
  `state` varchar(120) NOT NULL,
  `zipcode` varchar(120) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_useraddress_user_id_c954cb4_fk_orders_usercheckout_id` (`user_id`),
  CONSTRAINT `orders_useraddress_user_id_c954cb4_fk_orders_usercheckout_id` FOREIGN KEY (`user_id`) REFERENCES `orders_usercheckout` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of orders_useraddress
-- ----------------------------

-- ----------------------------
-- Table structure for `orders_usercheckout`
-- ----------------------------
DROP TABLE IF EXISTS `orders_usercheckout`;
CREATE TABLE `orders_usercheckout` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `wechatpay_id` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `orders_usercheckout_user_id_685d2891_fk_authwrapper_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `authwrapper_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of orders_usercheckout
-- ----------------------------

-- ----------------------------
-- Table structure for `personalcenter_userprofile`
-- ----------------------------
DROP TABLE IF EXISTS `personalcenter_userprofile`;
CREATE TABLE `personalcenter_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `score` decimal(10,0) NOT NULL,
  `level` decimal(10,0) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of personalcenter_userprofile
-- ----------------------------
INSERT INTO `personalcenter_userprofile` VALUES ('1', '1', '0', '0');

-- ----------------------------
-- Table structure for `phone_login_phonetoken`
-- ----------------------------
DROP TABLE IF EXISTS `phone_login_phonetoken`;
CREATE TABLE `phone_login_phonetoken` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone_number` varchar(128) NOT NULL,
  `otp` varchar(40) NOT NULL,
  `timestamp` datetime NOT NULL,
  `attempts` int(11) NOT NULL,
  `used` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of phone_login_phonetoken
-- ----------------------------

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
  CONSTRAINT `products_product_cat_category_id_dbc11ca_fk_products_category_id` FOREIGN KEY (`category_id`) REFERENCES `products_category` (`id`),
  CONSTRAINT `products_product_cate_product_id_5e61b960_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
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
INSERT INTO `products_productfeatured` VALUES ('8', 'products/featured/iphone/iphone-22-8-8.jpg', 'iPhone', '', '0', '', '0', '1', '1', '12');

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

-- ----------------------------
-- Table structure for `registration_registrationprofile`
-- ----------------------------
DROP TABLE IF EXISTS `registration_registrationprofile`;
CREATE TABLE `registration_registrationprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `activation_key` varchar(40) NOT NULL,
  `user_id` int(11) NOT NULL,
  `activated` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `registration_registrat_user_id_3f7685bb_fk_authwrapper_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `authwrapper_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of registration_registrationprofile
-- ----------------------------
