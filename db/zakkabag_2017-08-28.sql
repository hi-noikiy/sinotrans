/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 50512
Source Host           : localhost:3306
Source Database       : zakkabag

Target Server Type    : MYSQL
Target Server Version : 50512
File Encoding         : 65001

Date: 2017-08-28 08:49:56
*/

SET FOREIGN_KEY_CHECKS=0;

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
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of authwrapper_myuser
-- ----------------------------
INSERT INTO `authwrapper_myuser` VALUES ('1', 'pbkdf2_sha256$20000$xTcBg1XcKR9q$vn4xkcMq5Fya5hetrqSN2bP31r/fyw2Zxt1MwyCEhos=', '2017-08-25 13:50:21', '1', 'bhe001', '+8613500000000', 'Bin', 'He', 'bin.he@live.com', 'male', null, 'hebinn', '1', '1', '2017-07-09 13:19:00', 'phone', '');
INSERT INTO `authwrapper_myuser` VALUES ('42', 'pbkdf2_sha256$20000$LdqcjbJCu1WJ$ZVLHZwvY1/+mZeDp33TkeFKvzfNJW5fmczAXb7wJeiY=', '2017-08-12 05:56:02', '0', '13500000001', '+8613500000001', '', '', null, 'male', null, '', '0', '1', '2017-07-15 05:55:00', 'phone', 'upload\\1-160409144252927.jpg');
INSERT INTO `authwrapper_myuser` VALUES ('43', 'pbkdf2_sha256$20000$aQYAdoWXcyPg$KJIYAKLDa1hPhNgo+1dQ5/MZ3uRaHvnSeXQvc2tD0+I=', '2017-07-16 01:13:22', '0', '13600000000', '+8613600000000', '', '', null, 'male', '2017-07-15', '', '1', '1', '2017-07-15 05:56:00', 'phone', '');
INSERT INTO `authwrapper_myuser` VALUES ('44', 'pbkdf2_sha256$20000$TmRmDeFKp2JM$gRAzEr7qkhkdrIcdYcTisw8ajNbTTtY1FnUysB2Owmo=', null, '0', '+8613700000000', '+8613700000000', '', '', null, 'male', null, '', '0', '0', '2017-07-15 05:58:29', 'phone', '');
INSERT INTO `authwrapper_myuser` VALUES ('45', 'pbkdf2_sha256$20000$etHAFBKua3PB$lIW+BySQssQu6EtOg0ZsljrUhsoJ2EJIoBeiAnDqshk=', '2017-07-15 09:59:37', '0', '+8613900000000', '+8613900000000', '', '', null, 'male', '2017-07-15', '', '0', '1', '2017-07-15 09:59:32', 'phone', '');
INSERT INTO `authwrapper_myuser` VALUES ('46', 'pbkdf2_sha256$20000$93zTmTq4YfKU$+7qsSsjGSJnvn88NoaqAHpQuFTrUWW0ReH49DFT/bUk=', '2017-07-15 10:03:00', '0', '+8613901234567', '+8613901234567', '', '', null, 'male', '2017-07-15', '', '0', '1', '2017-07-15 10:02:40', 'phone', 'profile/+8613901234567/1029263936-0-46.jpg');

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
  CONSTRAINT `authwrapper_myuser_groups_group_id_4fd1194d_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `authwrapper_myuser_g_myuser_id_673733be_fk_authwrapper_myuser_id` FOREIGN KEY (`myuser_id`) REFERENCES `authwrapper_myuser` (`id`)
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of authwrapper_wechatuserprofile
-- ----------------------------
INSERT INTO `authwrapper_wechatuserprofile` VALUES ('4', 'o3J4ouMvqukm14tMqlugOT22_A_4', 'oS1RIv4sBIehckRXN5rn_TPZIy7Q', null, 'http://wx.qlogo.cn/mmhead/Q3auHgzwzM78RNe3LKwlXrMAZkBhr58yHqOuZjttx5sPRxkBmIQhlQ/0', 'hebinn', 'male', 'Songjiang', 'CN', 'zh_CN', null);

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------
INSERT INTO `auth_group` VALUES ('1', '1');

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
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------
INSERT INTO `auth_group_permissions` VALUES ('1', '1', '8');

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
) ENGINE=InnoDB AUTO_INCREMENT=152 DEFAULT CHARSET=utf8;

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
INSERT INTO `auth_permission` VALUES ('19', 'Can add sign up', '7', 'add_signup');
INSERT INTO `auth_permission` VALUES ('20', 'Can change sign up', '7', 'change_signup');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete sign up', '7', 'delete_signup');
INSERT INTO `auth_permission` VALUES ('25', 'Can add product', '9', 'add_product');
INSERT INTO `auth_permission` VALUES ('26', 'Can change product', '9', 'change_product');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete product', '9', 'delete_product');
INSERT INTO `auth_permission` VALUES ('28', 'Can add variation', '10', 'add_variation');
INSERT INTO `auth_permission` VALUES ('29', 'Can change variation', '10', 'change_variation');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete variation', '10', 'delete_variation');
INSERT INTO `auth_permission` VALUES ('31', 'Can add product image', '11', 'add_productimage');
INSERT INTO `auth_permission` VALUES ('32', 'Can change product image', '11', 'change_productimage');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete product image', '11', 'delete_productimage');
INSERT INTO `auth_permission` VALUES ('34', 'Can add category', '12', 'add_category');
INSERT INTO `auth_permission` VALUES ('35', 'Can change category', '12', 'change_category');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete category', '12', 'delete_category');
INSERT INTO `auth_permission` VALUES ('37', 'Can add product featured', '13', 'add_productfeatured');
INSERT INTO `auth_permission` VALUES ('38', 'Can change product featured', '13', 'change_productfeatured');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete product featured', '13', 'delete_productfeatured');
INSERT INTO `auth_permission` VALUES ('40', 'Can add cart item', '14', 'add_cartitem');
INSERT INTO `auth_permission` VALUES ('41', 'Can change cart item', '14', 'change_cartitem');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete cart item', '14', 'delete_cartitem');
INSERT INTO `auth_permission` VALUES ('43', 'Can add cart', '15', 'add_cart');
INSERT INTO `auth_permission` VALUES ('44', 'Can change cart', '15', 'change_cart');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete cart', '15', 'delete_cart');
INSERT INTO `auth_permission` VALUES ('46', 'Can add user checkout', '16', 'add_usercheckout');
INSERT INTO `auth_permission` VALUES ('47', 'Can change user checkout', '16', 'change_usercheckout');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete user checkout', '16', 'delete_usercheckout');
INSERT INTO `auth_permission` VALUES ('49', 'Can add user address', '17', 'add_useraddress');
INSERT INTO `auth_permission` VALUES ('50', 'Can change user address', '17', 'change_useraddress');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete user address', '17', 'delete_useraddress');
INSERT INTO `auth_permission` VALUES ('52', 'Can add order', '18', 'add_order');
INSERT INTO `auth_permission` VALUES ('53', 'Can change order', '18', 'change_order');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete order', '18', 'delete_order');
INSERT INTO `auth_permission` VALUES ('61', 'Can add registration profile', '21', 'add_registrationprofile');
INSERT INTO `auth_permission` VALUES ('62', 'Can change registration profile', '21', 'change_registrationprofile');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete registration profile', '21', 'delete_registrationprofile');
INSERT INTO `auth_permission` VALUES ('64', 'Can add Threaded comment', '22', 'add_threadedcomment');
INSERT INTO `auth_permission` VALUES ('65', 'Can change Threaded comment', '22', 'change_threadedcomment');
INSERT INTO `auth_permission` VALUES ('66', 'Can delete Threaded comment', '22', 'delete_threadedcomment');
INSERT INTO `auth_permission` VALUES ('67', 'Can add comment', '23', 'add_comment');
INSERT INTO `auth_permission` VALUES ('68', 'Can change comment', '23', 'change_comment');
INSERT INTO `auth_permission` VALUES ('69', 'Can delete comment', '23', 'delete_comment');
INSERT INTO `auth_permission` VALUES ('70', 'Can moderate comments', '23', 'can_moderate');
INSERT INTO `auth_permission` VALUES ('71', 'Can add comment flag', '24', 'add_commentflag');
INSERT INTO `auth_permission` VALUES ('72', 'Can change comment flag', '24', 'change_commentflag');
INSERT INTO `auth_permission` VALUES ('73', 'Can delete comment flag', '24', 'delete_commentflag');
INSERT INTO `auth_permission` VALUES ('74', 'Can add crowdfunding', '25', 'add_crowdfunding');
INSERT INTO `auth_permission` VALUES ('75', 'Can change crowdfunding', '25', 'change_crowdfunding');
INSERT INTO `auth_permission` VALUES ('76', 'Can delete crowdfunding', '25', 'delete_crowdfunding');
INSERT INTO `auth_permission` VALUES ('77', 'Can add mptt comment', '26', 'add_mpttcomment');
INSERT INTO `auth_permission` VALUES ('78', 'Can change mptt comment', '26', 'change_mpttcomment');
INSERT INTO `auth_permission` VALUES ('79', 'Can delete mptt comment', '26', 'delete_mpttcomment');
INSERT INTO `auth_permission` VALUES ('80', 'Can add user profile', '27', 'add_userprofile');
INSERT INTO `auth_permission` VALUES ('81', 'Can change user profile', '27', 'change_userprofile');
INSERT INTO `auth_permission` VALUES ('82', 'Can delete user profile', '27', 'delete_userprofile');
INSERT INTO `auth_permission` VALUES ('83', 'Can add banner', '28', 'add_banner');
INSERT INTO `auth_permission` VALUES ('84', 'Can change banner', '28', 'change_banner');
INSERT INTO `auth_permission` VALUES ('85', 'Can delete banner', '28', 'delete_banner');
INSERT INTO `auth_permission` VALUES ('86', 'Can add article', '29', 'add_article');
INSERT INTO `auth_permission` VALUES ('87', 'Can change article', '29', 'change_article');
INSERT INTO `auth_permission` VALUES ('88', 'Can delete article', '29', 'delete_article');
INSERT INTO `auth_permission` VALUES ('89', 'Can add user', '30', 'add_myuser');
INSERT INTO `auth_permission` VALUES ('90', 'Can change user', '30', 'change_myuser');
INSERT INTO `auth_permission` VALUES ('91', 'Can delete user', '30', 'delete_myuser');
INSERT INTO `auth_permission` VALUES ('92', 'Can add wechat user profile', '31', 'add_wechatuserprofile');
INSERT INTO `auth_permission` VALUES ('93', 'Can change wechat user profile', '31', 'change_wechatuserprofile');
INSERT INTO `auth_permission` VALUES ('94', 'Can delete wechat user profile', '31', 'delete_wechatuserprofile');
INSERT INTO `auth_permission` VALUES ('95', 'Can add OTP Token', '32', 'add_phonetoken');
INSERT INTO `auth_permission` VALUES ('96', 'Can change OTP Token', '32', 'change_phonetoken');
INSERT INTO `auth_permission` VALUES ('97', 'Can delete OTP Token', '32', 'delete_phonetoken');
INSERT INTO `auth_permission` VALUES ('98', 'Can add office inspection', '33', 'add_officeinspection');
INSERT INTO `auth_permission` VALUES ('99', 'Can change office inspection', '33', 'change_officeinspection');
INSERT INTO `auth_permission` VALUES ('100', 'Can delete office inspection', '33', 'delete_officeinspection');
INSERT INTO `auth_permission` VALUES ('101', 'Can add daily inspection', '34', 'add_dailyinspection');
INSERT INTO `auth_permission` VALUES ('102', 'Can change daily inspection', '34', 'change_dailyinspection');
INSERT INTO `auth_permission` VALUES ('103', 'Can delete daily inspection', '34', 'delete_dailyinspection');
INSERT INTO `auth_permission` VALUES ('104', 'Can add forklift', '35', 'add_forklift');
INSERT INTO `auth_permission` VALUES ('105', 'Can change forklift', '35', 'change_forklift');
INSERT INTO `auth_permission` VALUES ('106', 'Can delete forklift', '35', 'delete_forklift');
INSERT INTO `auth_permission` VALUES ('107', 'Can add forklift_image', '36', 'add_forklift_image');
INSERT INTO `auth_permission` VALUES ('108', 'Can change forklift_image', '36', 'change_forklift_image');
INSERT INTO `auth_permission` VALUES ('109', 'Can delete forklift_image', '36', 'delete_forklift_image');
INSERT INTO `auth_permission` VALUES ('110', 'Can add forklift_maint', '37', 'add_forklift_maint');
INSERT INTO `auth_permission` VALUES ('111', 'Can change forklift_maint', '37', 'change_forklift_maint');
INSERT INTO `auth_permission` VALUES ('112', 'Can delete forklift_maint', '37', 'delete_forklift_maint');
INSERT INTO `auth_permission` VALUES ('113', 'Can add forklift_repair', '38', 'add_forklift_repair');
INSERT INTO `auth_permission` VALUES ('114', 'Can change forklift_repair', '38', 'change_forklift_repair');
INSERT INTO `auth_permission` VALUES ('115', 'Can delete forklift_repair', '38', 'delete_forklift_repair');
INSERT INTO `auth_permission` VALUES ('116', 'Can add forklift_annual_inspection', '39', 'add_forklift_annual_inspection');
INSERT INTO `auth_permission` VALUES ('117', 'Can change forklift_annual_inspection', '39', 'change_forklift_annual_inspection');
INSERT INTO `auth_permission` VALUES ('118', 'Can delete forklift_annual_inspection', '39', 'delete_forklift_annual_inspection');
INSERT INTO `auth_permission` VALUES ('119', 'Can add forklift_annual_inspection_image', '40', 'add_forklift_annual_inspection_image');
INSERT INTO `auth_permission` VALUES ('120', 'Can change forklift_annual_inspection_image', '40', 'change_forklift_annual_inspection_image');
INSERT INTO `auth_permission` VALUES ('121', 'Can delete forklift_annual_inspection_image', '40', 'delete_forklift_annual_inspection_image');
INSERT INTO `auth_permission` VALUES ('122', 'Can add shelf', '41', 'add_shelf');
INSERT INTO `auth_permission` VALUES ('123', 'Can change shelf', '41', 'change_shelf');
INSERT INTO `auth_permission` VALUES ('124', 'Can delete shelf', '41', 'delete_shelf');
INSERT INTO `auth_permission` VALUES ('125', 'Can add shelf_inspection_record', '42', 'add_shelf_inspection_record');
INSERT INTO `auth_permission` VALUES ('126', 'Can change shelf_inspection_record', '42', 'change_shelf_inspection_record');
INSERT INTO `auth_permission` VALUES ('127', 'Can delete shelf_inspection_record', '42', 'delete_shelf_inspection_record');
INSERT INTO `auth_permission` VALUES ('128', 'Can add shelf_annual_inspection', '43', 'add_shelf_annual_inspection');
INSERT INTO `auth_permission` VALUES ('129', 'Can change shelf_annual_inspection', '43', 'change_shelf_annual_inspection');
INSERT INTO `auth_permission` VALUES ('130', 'Can delete shelf_annual_inspection', '43', 'delete_shelf_annual_inspection');
INSERT INTO `auth_permission` VALUES ('131', 'Can add shelf_annual_inspection_image', '44', 'add_shelf_annual_inspection_image');
INSERT INTO `auth_permission` VALUES ('132', 'Can change shelf_annual_inspection_image', '44', 'change_shelf_annual_inspection_image');
INSERT INTO `auth_permission` VALUES ('133', 'Can delete shelf_annual_inspection_image', '44', 'delete_shelf_annual_inspection_image');
INSERT INTO `auth_permission` VALUES ('134', 'Can add extinguisher', '45', 'add_extinguisher');
INSERT INTO `auth_permission` VALUES ('135', 'Can change extinguisher', '45', 'change_extinguisher');
INSERT INTO `auth_permission` VALUES ('136', 'Can delete extinguisher', '45', 'delete_extinguisher');
INSERT INTO `auth_permission` VALUES ('137', 'Can add hydrant', '46', 'add_hydrant');
INSERT INTO `auth_permission` VALUES ('138', 'Can change hydrant', '46', 'change_hydrant');
INSERT INTO `auth_permission` VALUES ('139', 'Can delete hydrant', '46', 'delete_hydrant');
INSERT INTO `auth_permission` VALUES ('140', 'Can add rehearsal', '47', 'add_rehearsal');
INSERT INTO `auth_permission` VALUES ('141', 'Can change rehearsal', '47', 'change_rehearsal');
INSERT INTO `auth_permission` VALUES ('142', 'Can delete rehearsal', '47', 'delete_rehearsal');
INSERT INTO `auth_permission` VALUES ('143', 'Can add extinguisher_inspection', '48', 'add_extinguisher_inspection');
INSERT INTO `auth_permission` VALUES ('144', 'Can change extinguisher_inspection', '48', 'change_extinguisher_inspection');
INSERT INTO `auth_permission` VALUES ('145', 'Can delete extinguisher_inspection', '48', 'delete_extinguisher_inspection');
INSERT INTO `auth_permission` VALUES ('146', 'Can add hydrant_inspection', '49', 'add_hydrant_inspection');
INSERT INTO `auth_permission` VALUES ('147', 'Can change hydrant_inspection', '49', 'change_hydrant_inspection');
INSERT INTO `auth_permission` VALUES ('148', 'Can delete hydrant_inspection', '49', 'delete_hydrant_inspection');
INSERT INTO `auth_permission` VALUES ('149', 'Can add shelf_inspection', '50', 'add_shelf_inspection');
INSERT INTO `auth_permission` VALUES ('150', 'Can change shelf_inspection', '50', 'change_shelf_inspection');
INSERT INTO `auth_permission` VALUES ('151', 'Can delete shelf_inspection', '50', 'delete_shelf_inspection');

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
  CONSTRAINT `carts_cart_user_id_4cb3f9df_fk_personalcenter_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `personalcenter_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of carts_cart
-- ----------------------------
INSERT INTO `carts_cart` VALUES ('1', '2016-11-29 14:40:39', '2016-11-29 14:40:39', null, '25.00', '1.88', '26.88', '0.07500');
INSERT INTO `carts_cart` VALUES ('2', '2016-12-03 01:47:45', '2017-04-29 00:52:20', '1', '0.00', '0.00', '0.00', '0.07500');
INSERT INTO `carts_cart` VALUES ('4', '2016-12-03 12:58:01', '2016-12-03 12:58:09', '1', '25.00', '1.88', '26.88', '0.07500');
INSERT INTO `carts_cart` VALUES ('5', '2017-03-15 15:02:17', '2017-04-29 00:52:20', '1', '0.00', '0.00', '0.00', '0.07500');
INSERT INTO `carts_cart` VALUES ('6', '2017-03-15 16:11:51', '2017-04-29 00:52:20', '1', '0.00', '0.00', '0.00', '0.07500');
INSERT INTO `carts_cart` VALUES ('7', '2017-03-26 09:51:59', '2017-04-29 00:52:20', '1', '0.00', '0.00', '0.00', '0.07500');
INSERT INTO `carts_cart` VALUES ('8', '2017-03-26 14:13:35', '2017-04-29 00:52:20', '1', '0.00', '0.00', '0.00', '0.07500');
INSERT INTO `carts_cart` VALUES ('9', '2017-03-26 14:29:18', '2017-04-29 00:52:20', '1', '0.00', '0.00', '0.00', '0.07500');
INSERT INTO `carts_cart` VALUES ('10', '2017-03-26 14:57:50', '2017-04-29 00:52:20', '1', '0.00', '0.00', '0.00', '0.07500');
INSERT INTO `carts_cart` VALUES ('11', '2017-05-01 23:54:53', '2017-05-01 23:54:58', '1', '300.00', '22.50', '322.50', '0.07500');
INSERT INTO `carts_cart` VALUES ('12', '2017-07-15 06:55:01', '2017-07-15 06:55:01', '1', '25.00', '1.88', '26.88', '0.07500');

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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of carts_cartitem
-- ----------------------------
INSERT INTO `carts_cartitem` VALUES ('9', '1', '11', '9', '300.00');

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
  CONSTRAINT `comments_mpttcomme_comment_ptr_id_4e1103e4_fk_django_comments_id` FOREIGN KEY (`comment_ptr_id`) REFERENCES `django_comments` (`id`),
  CONSTRAINT `commen_parent_id_57eaa83b_fk_comments_mpttcomment_comment_ptr_id` FOREIGN KEY (`parent_id`) REFERENCES `comments_mpttcomment` (`comment_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of comments_mpttcomment
-- ----------------------------
INSERT INTO `comments_mpttcomment` VALUES ('918', '1', '8', '1', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('919', '1', '2', '2', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('920', '1', '2', '3', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('921', '1', '2', '4', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('922', '1', '2', '5', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('925', '1', '2', '6', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('926', '1', '2', '7', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('927', '1', '2', '8', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('929', '1', '2', '9', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('930', '1', '2', '10', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('931', '1', '2', '11', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('932', '1', '2', '12', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('933', '1', '2', '13', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('934', '1', '2', '14', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('935', '2', '3', '1', '1', '918');
INSERT INTO `comments_mpttcomment` VALUES ('936', '4', '7', '1', '1', '918');
INSERT INTO `comments_mpttcomment` VALUES ('937', '5', '6', '1', '2', '936');
INSERT INTO `comments_mpttcomment` VALUES ('938', '1', '2', '15', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('939', '1', '2', '16', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('940', '1', '2', '17', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('941', '1', '2', '17', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('944', '1', '2', '18', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('945', '1', '2', '19', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('946', '1', '2', '20', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('947', '1', '2', '21', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('950', '1', '2', '22', '0', null);
INSERT INTO `comments_mpttcomment` VALUES ('951', '1', '2', '23', '0', null);

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
  KEY `crowdfundings_crowd_user_id_4896770f_fk_personalcenter_myuser_id` (`user_id`),
  CONSTRAINT `crowdfundings_crowd_user_id_4896770f_fk_personalcenter_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `personalcenter_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crowdfundings_crowdfunding
-- ----------------------------
INSERT INTO `crowdfundings_crowdfunding` VALUES ('1', 'health', 'test', 'test', '1', 'crowdfunding/bhe001/1-test.gif', '2016-12-04 14:26:00', '1', '100', '2016-12-24 07:03:21');
INSERT INTO `crowdfundings_crowdfunding` VALUES ('6', 'health', 'iPhone', 'test', '0', 'crowdfunding/bhe001/None-iphone_PHY2YCf.jpg', '2016-12-24 07:42:00', '1', '100', '2016-12-24 07:42:00');
INSERT INTO `crowdfundings_crowdfunding` VALUES ('12', 'health', 'test', 'test', '0', 'crowdfunding/bhe001/None-test_MNg73TQ.jpg', '2016-12-24 08:16:00', '1', '100', '2016-12-24 08:16:00');
INSERT INTO `crowdfundings_crowdfunding` VALUES ('13', 'health', 'test', 'test', '0', 'crowdfunding/bhe001/None-test_Aw18G8J.jpg', '2016-12-24 08:16:00', '1', '100', '2016-12-24 08:16:00');
INSERT INTO `crowdfundings_crowdfunding` VALUES ('14', 'health', 'test', 'test', '0', 'crowdfunding/bhe001/None-test_SxsIk6F.jpg', '2016-12-24 08:18:00', '1', '100', '2016-12-24 08:18:00');
INSERT INTO `crowdfundings_crowdfunding` VALUES ('15', 'health', 'test', 'test', '0', 'crowdfunding/bhe001/None-test_8MYFj0P.jpg', '2016-12-24 08:18:00', '1', '100', '2016-12-24 08:18:00');
INSERT INTO `crowdfundings_crowdfunding` VALUES ('16', 'health', 'test', 'test', '0', 'crowdfunding/bhe001/None-test_vDCf99W.jpg', '2016-12-24 08:18:00', '1', '100', '2016-12-24 08:18:00');
INSERT INTO `crowdfundings_crowdfunding` VALUES ('17', 'health', 'test', 'test', '1', 'crowdfunding/bhe001/None-test_cgxbsgD.jpg', '2016-12-24 08:20:00', '1', '100', '2016-12-24 08:20:00');
INSERT INTO `crowdfundings_crowdfunding` VALUES ('18', 'health', 'test', 'test', '0', 'crowdfunding/bhe001/test-None.jpg', '2017-07-15 13:28:00', '1', '100', '2017-07-15 13:28:00');

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
  KEY `django_admin_log_user_id_1c5f563_fk_personalcenter_myuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_personalcenter_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `personalcenter_myuser` (`id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1347 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('18', '2016-12-03 01:32:59', '1', 'electronics', '1', '', '12', '1');
INSERT INTO `django_admin_log` VALUES ('19', '2016-12-03 01:34:13', '1', 'p1', '1', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('20', '2016-12-03 01:35:06', '1', 'p1', '1', '', '13', '1');
INSERT INTO `django_admin_log` VALUES ('22', '2016-12-03 06:09:38', '2', 'Donate', '1', '', '12', '1');
INSERT INTO `django_admin_log` VALUES ('23', '2016-12-03 07:19:52', '2', 'p1', '1', '', '13', '1');
INSERT INTO `django_admin_log` VALUES ('24', '2016-12-03 07:20:06', '3', 'p1', '1', '', '13', '1');
INSERT INTO `django_admin_log` VALUES ('25', '2016-12-03 07:20:19', '4', 'p1', '1', '', '13', '1');
INSERT INTO `django_admin_log` VALUES ('26', '2016-12-03 07:35:20', '4', 'p1', '2', '已修改 image 。', '13', '1');
INSERT INTO `django_admin_log` VALUES ('27', '2016-12-03 07:35:25', '3', 'p1', '2', '已修改 image 。', '13', '1');
INSERT INTO `django_admin_log` VALUES ('28', '2016-12-03 07:35:31', '2', 'p1', '2', '已修改 image 。', '13', '1');
INSERT INTO `django_admin_log` VALUES ('29', '2016-12-03 07:35:42', '1', 'p1', '2', '已修改 image 。', '13', '1');
INSERT INTO `django_admin_log` VALUES ('30', '2016-12-03 08:26:34', '1', 'p1', '2', '已修改 image 。', '13', '1');
INSERT INTO `django_admin_log` VALUES ('32', '2016-12-04 14:26:40', '1', 'test', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('33', '2016-12-10 02:15:40', '2', '123456', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('34', '2016-12-10 02:42:24', '2', '123456', '2', '已修改 detail 。', '25', '1');
INSERT INTO `django_admin_log` VALUES ('35', '2016-12-10 09:49:25', '5', 'Bin3 He2: dfs...', '3', '', '23', '1');
INSERT INTO `django_admin_log` VALUES ('36', '2016-12-10 09:49:25', '4', 'Bin3 He2: csdong...', '3', '', '23', '1');
INSERT INTO `django_admin_log` VALUES ('37', '2016-12-10 09:49:25', '3', 'Bin3 He2: fsds...', '3', '', '23', '1');
INSERT INTO `django_admin_log` VALUES ('38', '2016-12-10 09:49:25', '2', 'Bin3 He2: dfsddfsdfsdfsdf...', '3', '', '23', '1');
INSERT INTO `django_admin_log` VALUES ('39', '2016-12-10 09:49:25', '1', 'Bin3 He2: dfsfd...', '3', '', '23', '1');
INSERT INTO `django_admin_log` VALUES ('40', '2016-12-11 01:48:58', '3', 'test', '1', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('41', '2016-12-17 12:39:27', '36', 'Bin3 He2: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('42', '2016-12-17 12:39:27', '37', 'Bin3 He2: 123456...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('43', '2016-12-17 12:39:27', '38', 'Bin3 He2: 789...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('44', '2016-12-17 12:39:27', '46', 'csdong: lalala...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('45', '2016-12-17 12:39:27', '47', 'csdong: lalalalalallal...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('46', '2016-12-17 12:39:27', '48', 'csdong: lafj...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('47', '2016-12-17 12:39:27', '49', 'csdong: xxxxxx...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('48', '2016-12-17 12:39:27', '50', 'Bin3 He2: xxxx...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('49', '2016-12-17 12:39:27', '51', 'Bin3 He2: yyyyyyy...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('50', '2016-12-17 12:39:27', '52', 'Bin3 He2: zzz...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('51', '2016-12-17 12:39:27', '53', 'Bin3 He2: www...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('52', '2016-12-17 12:39:27', '54', 'Bin3 He2: ttt...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('53', '2016-12-17 12:39:27', '55', 'Bin3 He2: zzz...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('54', '2016-12-17 12:39:27', '56', 'Bin3 He2: ttt...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('55', '2016-12-17 12:39:27', '57', 'csdong: mmmm...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('56', '2016-12-17 12:39:27', '58', 'csdong: nnn...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('57', '2016-12-17 12:39:27', '59', 'csdong: xxxxxx...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('58', '2016-12-17 12:39:27', '60', 'csdong: adasdasda...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('59', '2016-12-17 13:27:57', '8', 'Bin3 He2: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('60', '2016-12-17 13:27:57', '11', 'Bin3 He2: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('61', '2016-12-17 13:27:57', '14', 'Bin3 He2: 14...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('62', '2016-12-17 13:27:58', '9', 'Bin3 He2: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('63', '2016-12-17 13:27:58', '12', 'Bin3 He2: 12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('64', '2016-12-17 13:27:58', '13', 'Bin3 He2: 13...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('65', '2016-12-17 13:27:58', '20', 'Bin3 He2: 20...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('66', '2016-12-17 13:27:58', '10', 'Bin3 He2: 10...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('67', '2016-12-17 13:27:58', '15', 'Bin3 He2: 15...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('68', '2016-12-17 13:27:58', '16', 'Bin3 He2: 16...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('69', '2016-12-17 13:27:58', '17', 'Bin3 He2: 17...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('70', '2016-12-17 13:27:58', '21', 'Bin3 He2: 21...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('71', '2016-12-17 13:27:58', '24', 'Bin3 He2: 22...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('72', '2016-12-17 13:27:58', '19', 'Bin3 He2: 19...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('73', '2016-12-17 13:27:58', '18', 'Bin3 He2: 18...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('74', '2016-12-17 13:27:58', '22', 'Bin3 He2: 22...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('75', '2016-12-17 13:27:58', '23', 'Bin3 He2: 23...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('76', '2016-12-17 13:27:58', '25', 'Bin3 He2: 25...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('77', '2016-12-17 13:27:58', '26', 'Bin3 He2: 26...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('78', '2016-12-17 13:27:58', '27', 'Bin3 He2: 27...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('79', '2016-12-17 13:27:58', '28', 'Bin3 He2: 28...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('80', '2016-12-17 13:27:58', '29', 'Bin3 He2: 29...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('81', '2016-12-17 13:27:58', '31', 'Bin3 He2: 31...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('82', '2016-12-17 13:27:58', '30', 'Bin3 He2: 30...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('83', '2016-12-17 13:27:58', '32', 'Bin3 He2: 33...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('84', '2016-12-17 13:27:58', '33', 'csdong: fsfsd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('85', '2016-12-17 13:27:58', '39', 'Bin3 He2: 001...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('86', '2016-12-17 13:27:59', '40', 'Bin3 He2: 002...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('87', '2016-12-17 13:27:59', '41', 'Bin3 He2: 003...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('88', '2016-12-17 13:27:59', '42', 'Bin3 He2: 004...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('89', '2016-12-17 13:27:59', '43', 'Bin3 He2: 005...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('90', '2016-12-17 13:27:59', '44', 'Bin3 He2: 006...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('91', '2016-12-17 13:27:59', '45', 'Bin3 He2: 007...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('92', '2016-12-17 13:27:59', '34', '37: 37...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('93', '2016-12-17 13:27:59', '35', '38: 38...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('94', '2016-12-17 13:27:59', '61', 'Bin3 He2: 008...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('95', '2016-12-17 13:27:59', '62', 'Bin3 He2: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('96', '2016-12-17 13:27:59', '63', 'Bin3 He2: 456...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('97', '2016-12-17 13:27:59', '64', 'Bin3 He2: 126...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('98', '2016-12-17 14:10:44', '65', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('99', '2016-12-17 14:10:44', '66', 'Bin3 He2: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('100', '2016-12-17 14:10:44', '67', 'csdong: 123456...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('101', '2016-12-17 14:10:44', '68', '1: 23131...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('102', '2016-12-17 14:10:44', '69', 'example: 424234...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('103', '2016-12-17 14:10:44', '70', '1: 4342423...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('104', '2016-12-17 14:10:44', '71', '1: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('105', '2016-12-17 14:10:44', '72', 'example: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('106', '2016-12-17 14:10:44', '73', 'csdong: 1234...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('107', '2016-12-17 14:10:44', '74', '1: 12345...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('108', '2016-12-17 14:10:44', '75', 'example: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('109', '2016-12-17 14:10:44', '76', '1: 1234...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('110', '2016-12-17 14:10:44', '77', 'example: 134...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('111', '2016-12-17 14:10:45', '78', '1: 1234567...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('112', '2016-12-17 14:10:45', '79', 'example: 1234sdfs...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('113', '2016-12-17 14:28:46', '80', 'Bin3 He2: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('114', '2016-12-17 14:28:46', '81', 'Bin3 He2: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('115', '2016-12-17 14:28:46', '82', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('116', '2016-12-17 14:28:46', '83', 'Bin3 He2: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('117', '2016-12-17 14:28:46', '84', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('118', '2016-12-17 14:28:46', '85', 'Bin3 He2: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('119', '2016-12-17 14:28:46', '86', 'Bin3 He2: 1234...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('120', '2016-12-17 14:28:46', '87', 'Bin3 He2: 12345...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('121', '2016-12-17 14:28:46', '88', 'Bin3 He2: 126...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('122', '2016-12-17 14:28:46', '89', 'Bin3 He2: ty...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('123', '2016-12-17 14:53:25', '90', 'Bin3 He2: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('124', '2016-12-17 14:53:25', '91', 'Bin3 He2: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('125', '2016-12-17 14:53:25', '92', 'Bin3 He2: 1234...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('126', '2016-12-17 14:53:25', '93', 'Bin3 He2: 13579...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('127', '2016-12-17 14:53:25', '94', 'Bin3 He2: 134...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('128', '2016-12-17 14:53:25', '95', 'Bin3 He2: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('129', '2016-12-17 14:53:25', '96', 'Bin3 He2: 567...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('130', '2016-12-17 14:53:25', '98', 'Bin3 He2: ghj...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('131', '2016-12-17 14:53:25', '97', 'Bin3 He2: rty...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('132', '2016-12-17 15:25:41', '99', 'Bin3 He2: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('133', '2016-12-17 15:25:41', '100', 'Bin3 He2: 1234...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('134', '2016-12-17 15:25:41', '102', 'Bin3 He2: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('135', '2016-12-17 15:25:41', '111', 'Bin3 He2: tyu...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('136', '2016-12-17 15:25:41', '101', 'Bin3 He2: 567...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('137', '2016-12-17 15:25:41', '103', 'Bin3 He2: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('138', '2016-12-17 15:25:42', '104', 'Bin3 He2: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('139', '2016-12-17 15:25:42', '105', 'Bin3 He2: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('140', '2016-12-17 15:25:42', '106', 'Bin3 He2: 1234...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('141', '2016-12-17 15:25:42', '107', 'Bin3 He2: 567...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('142', '2016-12-17 15:25:42', '110', 'Bin3 He2: ui...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('143', '2016-12-17 15:25:42', '108', 'Bin3 He2: 456...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('144', '2016-12-17 15:25:42', '109', 'Bin3 He2: 345...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('145', '2016-12-17 16:34:42', '112', 'Bin3 He2: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('146', '2016-12-17 16:34:42', '113', 'Bin3 He2: 456...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('147', '2016-12-17 16:34:42', '114', 'Bin3 He2: 567...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('148', '2016-12-17 16:34:42', '115', 'Bin3 He2: tyu...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('149', '2016-12-17 16:34:42', '116', 'Bin3 He2: fsfs...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('150', '2016-12-17 16:34:42', '117', 'Bin3 He2: fsafsfa...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('151', '2016-12-17 16:34:42', '118', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('152', '2016-12-17 16:34:42', '119', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('153', '2016-12-17 16:34:42', '120', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('154', '2016-12-17 16:34:42', '121', 'Bin3 He2: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('155', '2016-12-17 16:34:42', '122', 'Bin3 He2: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('156', '2016-12-17 16:34:42', '123', 'Bin3 He2: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('157', '2016-12-17 16:34:42', '124', 'Bin3 He2: rt...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('158', '2016-12-17 16:34:42', '127', 'Bin3 He2: dfs...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('159', '2016-12-17 16:34:42', '125', 'Bin3 He2: xx...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('160', '2016-12-17 16:34:42', '126', 'Bin3 He2: x...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('161', '2016-12-17 16:34:42', '128', 'Bin3 He2: x...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('162', '2016-12-17 16:34:42', '131', 'Bin3 He2: ff...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('163', '2016-12-17 16:34:42', '129', 'Bin3 He2: yy...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('164', '2016-12-17 16:34:42', '130', 'Bin3 He2: xxxx...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('165', '2016-12-17 16:34:42', '132', 'Bin3 He2: xxxxxxx...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('166', '2016-12-17 16:34:42', '133', 'Bin3 He2: xxx...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('167', '2016-12-17 16:34:42', '134', 'Bin3 He2: xxx...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('168', '2016-12-17 16:34:42', '135', 'Bin3 He2: xxxxx...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('169', '2016-12-17 16:34:42', '136', 'Bin3 He2: gg...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('170', '2016-12-17 16:34:42', '137', 'Bin3 He2: tt...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('171', '2016-12-17 16:34:43', '138', 'Bin3 He2: fdfd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('172', '2016-12-18 01:25:22', '139', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('173', '2016-12-18 01:25:23', '140', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('174', '2016-12-18 01:25:23', '141', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('175', '2016-12-18 01:25:23', '142', 'Bin3 He2: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('176', '2016-12-18 01:25:23', '143', 'Bin3 He2: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('177', '2016-12-18 01:25:23', '144', 'Bin3 He2: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('178', '2016-12-18 01:25:23', '145', 'Bin3 He2: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('179', '2016-12-18 01:25:23', '146', 'Bin3 He2: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('180', '2016-12-18 01:25:23', '147', 'Bin3 He2: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('181', '2016-12-18 01:25:23', '148', 'Bin3 He2: 10...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('182', '2016-12-18 02:18:31', '149', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('183', '2016-12-18 02:18:31', '150', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('184', '2016-12-18 02:18:31', '151', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('185', '2016-12-18 02:18:31', '152', 'Bin3 He2: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('186', '2016-12-18 02:18:31', '153', 'Bin3 He2: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('187', '2016-12-18 02:18:31', '154', 'Bin3 He2: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('188', '2016-12-18 02:18:31', '155', 'Bin3 He2: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('189', '2016-12-18 02:43:26', '156', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('190', '2016-12-18 02:43:26', '157', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('191', '2016-12-18 02:43:26', '158', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('192', '2016-12-18 02:43:26', '159', 'Bin3 He2: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('193', '2016-12-18 02:43:26', '160', 'Bin3 He2: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('194', '2016-12-18 02:43:26', '161', 'Bin3 He2: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('195', '2016-12-18 02:43:26', '162', 'Bin3 He2: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('196', '2016-12-18 03:04:23', '163', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('197', '2016-12-18 03:04:23', '164', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('198', '2016-12-18 03:04:23', '165', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('199', '2016-12-18 03:04:23', '166', 'Bin3 He2: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('200', '2016-12-18 03:04:23', '167', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('201', '2016-12-18 07:23:31', '168', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('202', '2016-12-18 07:23:31', '169', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('203', '2016-12-18 07:23:31', '170', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('204', '2016-12-18 07:23:31', '171', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('205', '2016-12-18 07:23:32', '172', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('206', '2016-12-18 07:23:32', '173', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('207', '2016-12-18 07:23:32', '174', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('208', '2016-12-18 07:23:32', '175', 'Bin3 He2: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('209', '2016-12-18 07:23:32', '176', 'Bin3 He2: 22...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('210', '2016-12-18 07:23:32', '177', 'Bin3 He2: 22...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('211', '2016-12-18 07:23:32', '178', 'Bin3 He2: 33...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('212', '2016-12-18 07:23:32', '179', 'Bin3 He2: 34...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('213', '2016-12-18 07:23:32', '180', 'Bin3 He2: 34...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('214', '2016-12-18 07:23:32', '181', 'Bin3 He2: 12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('215', '2016-12-18 07:23:32', '182', 'Bin3 He2: 35...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('216', '2016-12-18 07:38:41', '183', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('217', '2016-12-18 07:38:41', '184', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('218', '2016-12-18 07:38:41', '185', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('219', '2016-12-18 07:38:41', '186', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('220', '2016-12-18 07:38:41', '187', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('221', '2016-12-18 07:38:41', '188', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('222', '2016-12-18 07:52:42', '189', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('223', '2016-12-18 07:52:43', '194', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('224', '2016-12-18 07:52:43', '195', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('225', '2016-12-18 07:52:43', '196', 'Bin3 He2: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('226', '2016-12-18 07:52:43', '197', 'Bin3 He2: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('227', '2016-12-18 07:52:43', '191', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('228', '2016-12-18 07:52:43', '192', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('229', '2016-12-18 07:52:43', '193', 'Bin3 He2: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('230', '2016-12-18 07:52:43', '198', 'Bin3 He2: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('231', '2016-12-18 07:52:43', '199', 'Bin3 He2: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('232', '2016-12-18 07:52:43', '200', 'Bin3 He2: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('233', '2016-12-18 07:52:43', '201', 'Bin3 He2: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('234', '2016-12-18 07:52:43', '202', 'Bin3 He2: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('235', '2016-12-18 08:13:46', '203', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('236', '2016-12-18 08:13:46', '204', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('237', '2016-12-18 08:13:46', '205', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('238', '2016-12-18 08:13:46', '206', 'Bin3 He2: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('239', '2016-12-18 08:13:46', '207', 'Bin3 He2: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('240', '2016-12-18 08:13:46', '208', 'Bin3 He2: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('241', '2016-12-18 08:13:46', '209', 'Bin3 He2: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('242', '2016-12-18 08:21:59', '210', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('243', '2016-12-18 08:21:59', '211', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('244', '2016-12-18 08:21:59', '212', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('245', '2016-12-18 08:21:59', '213', 'Bin3 He2: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('246', '2016-12-18 08:21:59', '214', 'Bin3 He2: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('247', '2016-12-18 08:21:59', '215', 'Bin3 He2: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('248', '2016-12-18 08:21:59', '216', 'Bin3 He2: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('249', '2016-12-18 08:21:59', '217', 'Bin3 He2: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('250', '2016-12-18 08:21:59', '218', 'Bin3 He2: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('251', '2016-12-18 08:21:59', '219', 'Bin3 He2: 10...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('252', '2016-12-18 08:22:00', '220', 'Bin3 He2: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('253', '2016-12-18 11:06:45', '221', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('254', '2016-12-18 11:06:45', '222', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('255', '2016-12-18 11:06:45', '223', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('256', '2016-12-18 11:06:45', '224', 'Bin3 He2: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('257', '2016-12-18 11:06:45', '225', 'Bin3 He2: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('258', '2016-12-18 11:09:14', '1', 'test', '2', '已修改 image 。', '25', '1');
INSERT INTO `django_admin_log` VALUES ('259', '2016-12-18 11:13:53', '226', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('260', '2016-12-18 11:13:53', '230', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('261', '2016-12-18 11:13:53', '231', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('262', '2016-12-18 11:13:53', '232', 'Bin3 He2: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('263', '2016-12-18 11:13:53', '233', 'Bin3 He2: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('264', '2016-12-18 11:13:53', '227', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('265', '2016-12-18 11:13:53', '228', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('266', '2016-12-18 11:13:53', '229', 'Bin3 He2: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('267', '2016-12-18 11:21:36', '234', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('268', '2016-12-18 11:21:36', '235', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('269', '2016-12-18 11:21:36', '236', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('270', '2016-12-18 11:21:36', '237', 'Bin3 He2: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('271', '2016-12-18 11:21:36', '238', 'Bin3 He2: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('272', '2016-12-18 11:58:54', '239', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('273', '2016-12-18 11:58:55', '241', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('274', '2016-12-18 11:58:55', '242', 'Bin3 He2: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('275', '2016-12-18 11:58:55', '240', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('276', '2016-12-18 11:58:55', '243', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('277', '2016-12-18 11:58:55', '244', 'Bin3 He2: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('278', '2016-12-18 11:58:55', '245', 'Bin3 He2: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('279', '2016-12-18 11:58:55', '246', 'Bin3 He2: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('280', '2016-12-18 11:58:55', '247', 'Bin3 He2: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('281', '2016-12-18 11:58:55', '248', 'Bin3 He2: 111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('282', '2016-12-18 11:58:55', '249', 'Bin3 He2: q...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('283', '2016-12-18 11:58:55', '250', 'Bin3 He2: xx...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('284', '2016-12-18 12:00:28', '254', 'Bin3 He2: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('285', '2016-12-18 12:00:28', '256', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('286', '2016-12-18 12:00:28', '257', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('287', '2016-12-18 12:00:28', '255', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('288', '2016-12-18 12:00:28', '252', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('289', '2016-12-18 12:00:28', '253', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('290', '2016-12-18 13:09:08', '251', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('291', '2016-12-18 13:09:08', '262', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('292', '2016-12-18 13:09:08', '276', 'Bin3 He2: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('293', '2016-12-18 13:09:09', '280', 'Bin3 He2: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('294', '2016-12-18 13:09:09', '281', 'Bin3 He2: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('295', '2016-12-18 13:09:09', '282', 'Bin3 He2: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('296', '2016-12-18 13:09:09', '283', 'Bin3 He2: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('297', '2016-12-18 13:09:09', '284', 'Bin3 He2: 10...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('298', '2016-12-18 13:09:09', '285', 'Bin3 He2: 12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('299', '2016-12-18 13:09:09', '286', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('300', '2016-12-18 13:09:09', '258', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('301', '2016-12-18 13:09:09', '259', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('302', '2016-12-18 13:09:09', '260', 'Bin3 He2: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('303', '2016-12-18 13:09:09', '261', 'Bin3 He2: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('304', '2016-12-18 13:09:09', '263', 'Bin3 He2: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('305', '2016-12-18 13:09:09', '264', 'Bin3 He2: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('306', '2016-12-18 13:09:09', '266', 'Bin3 He2: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('307', '2016-12-18 13:09:09', '267', 'Bin3 He2: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('308', '2016-12-18 13:09:09', '268', 'Bin3 He2: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('309', '2016-12-18 13:09:09', '271', 'Bin3 He2: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('310', '2016-12-18 13:09:09', '272', 'Bin3 He2: 10...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('311', '2016-12-18 13:09:09', '273', 'Bin3 He2: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('312', '2016-12-18 13:09:09', '274', 'Bin3 He2: 12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('313', '2016-12-18 13:09:09', '275', 'Bin3 He2: 13...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('314', '2016-12-18 13:09:09', '277', 'Bin3 He2: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('315', '2016-12-18 13:09:09', '278', 'Bin3 He2: 124...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('316', '2016-12-18 13:09:09', '279', 'Bin3 He2: 126...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('317', '2016-12-18 13:11:57', '287', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('318', '2016-12-18 13:11:57', '290', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('319', '2016-12-18 13:11:57', '291', 'Bin3 He2: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('320', '2016-12-18 13:11:57', '292', 'Bin3 He2: 111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('321', '2016-12-18 13:11:57', '293', 'Bin3 He2: 1111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('322', '2016-12-18 13:11:57', '294', 'Bin3 He2: 11111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('323', '2016-12-18 13:11:57', '296', 'Bin3 He2: 1212121...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('324', '2016-12-18 13:11:57', '295', 'Bin3 He2: 1212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('325', '2016-12-18 13:11:57', '288', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('326', '2016-12-18 13:11:57', '289', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('327', '2016-12-18 13:59:53', '297', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('328', '2016-12-18 13:59:53', '299', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('329', '2016-12-18 13:59:53', '300', 'Bin3 He2: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('330', '2016-12-18 13:59:53', '301', 'Bin3 He2: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('331', '2016-12-18 13:59:53', '302', 'Bin3 He2: 12121...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('332', '2016-12-18 13:59:53', '303', 'Bin3 He2: 22...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('333', '2016-12-18 13:59:53', '304', 'Bin3 He2: 121212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('334', '2016-12-18 13:59:53', '305', 'Bin3 He2: 121212121...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('335', '2016-12-18 13:59:53', '312', 'Bin3 He2: 111111111111111111111111111111111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('336', '2016-12-18 13:59:53', '313', 'Bin3 He2: 21212121...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('337', '2016-12-18 13:59:54', '314', 'Bin3 He2: 1212121212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('338', '2016-12-18 13:59:54', '315', 'Bin3 He2: fsfsdfsfs...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('339', '2016-12-18 13:59:54', '322', 'Bin3 He2: 1212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('340', '2016-12-18 13:59:54', '298', 'Bin3 He2: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('341', '2016-12-18 13:59:54', '306', 'Bin3 He2: 12121...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('342', '2016-12-18 13:59:54', '307', 'Bin3 He2: 1212121...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('343', '2016-12-18 13:59:54', '308', 'Bin3 He2: 1212121212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('344', '2016-12-18 13:59:54', '309', 'Bin3 He2: 2222...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('345', '2016-12-18 13:59:54', '310', 'Bin3 He2: 2222222222...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('346', '2016-12-18 13:59:54', '311', 'Bin3 He2: 3121212121...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('347', '2016-12-18 13:59:54', '316', 'Bin3 He2: 1212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('348', '2016-12-18 13:59:54', '318', 'Bin3 He2: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('349', '2016-12-18 13:59:54', '317', 'Bin3 He2: 12e1e12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('350', '2016-12-18 13:59:54', '319', 'Bin3 He2: 12eeeeeeeeeee...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('351', '2016-12-18 13:59:54', '320', 'Bin3 He2: 1211111111111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('352', '2016-12-18 13:59:54', '321', 'Bin3 He2: 121212121...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('353', '2016-12-24 08:03:17', '5', 'iPhone', '3', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('354', '2016-12-24 08:03:17', '4', 'iPhone', '3', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('355', '2016-12-24 08:03:17', '3', 'iPhone', '3', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('356', '2016-12-24 08:13:26', '9', 'test', '3', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('357', '2016-12-24 08:13:26', '8', 'test', '3', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('358', '2016-12-24 08:13:26', '7', 'test', '3', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('359', '2016-12-24 08:16:22', '11', 'test', '3', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('360', '2016-12-24 08:16:22', '10', 'test', '3', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('361', '2017-03-13 15:01:01', '1', 'p1', '2', '已变更 title for variation \"v2\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('362', '2017-03-13 15:01:29', '1', '32G', '2', '已修改 title 。', '9', '1');
INSERT INTO `django_admin_log` VALUES ('363', '2017-03-13 15:02:16', '1', 'iPhone', '2', '已修改 title 。 已变更 title for variation \"64G\". 已变更 title for variation \"32G\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('364', '2017-03-13 15:02:44', '2', 'iPhone', '2', '已修改 title 。', '9', '1');
INSERT INTO `django_admin_log` VALUES ('365', '2017-03-13 15:03:02', '1', 'desert', '2', '已修改 title 。', '9', '1');
INSERT INTO `django_admin_log` VALUES ('366', '2017-03-13 15:03:43', '1', 'desert', '2', '已变更 sale_price for variation \"64G\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('372', '2017-03-26 08:04:11', '1', '1', '1', '', '3', '1');
INSERT INTO `django_admin_log` VALUES ('373', '2017-03-26 09:50:25', '2', 'iPhone', '2', '已修改 description 。', '9', '1');
INSERT INTO `django_admin_log` VALUES ('374', '2017-03-26 15:42:25', '1', 'bhe001', '2', '已修改 score 和 level 。', '27', '1');
INSERT INTO `django_admin_log` VALUES ('377', '2017-04-29 00:48:00', '3', 'chair', '1', '', '12', '1');
INSERT INTO `django_admin_log` VALUES ('378', '2017-04-29 00:48:10', '4', 'Cofoe Commode Chair (ZC065)', '1', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('379', '2017-04-29 00:49:02', '4', 'Cofoe Commode Chair (ZC065)', '2', '已修改 default 。 已添加 product image \"Cofoe Commode Chair (ZC065)\". 已变更 title，sale_price 和 inventory for variation \"ZC065\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('380', '2017-04-29 00:50:12', '5', 'Cofoe Commode Chair (ZC018)', '1', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('381', '2017-04-29 00:50:31', '5', 'Cofoe Commode Chair (ZC018)', '2', '已变更 title，sale_price 和 inventory for variation \"ZC018\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('382', '2017-04-29 00:51:21', '6', 'Cofoe Commode Chair (ZC019)', '1', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('383', '2017-04-29 00:51:35', '6', 'Cofoe Commode Chair (ZC019)', '2', '已删除 variation \"Default\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('384', '2017-04-29 00:52:20', '3', 'iPhone', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('385', '2017-04-29 00:52:20', '2', 'iPhone', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('386', '2017-04-29 00:52:20', '1', 'desert', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('387', '2017-04-29 00:54:35', '7', 'Cofoe Commode Chair (ZC067)', '1', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('388', '2017-04-29 00:54:49', '7', 'Cofoe Commode Chair (ZC067)', '2', '已变更 title，sale_price 和 inventory for variation \"ZC067\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('389', '2017-04-29 00:57:11', '5', 'Cofoe Commode Chair (ZC067)', '1', '', '13', '1');
INSERT INTO `django_admin_log` VALUES ('390', '2017-04-29 00:58:21', '6', 'Cofoe Commode Chair (ZC065)', '1', '', '13', '1');
INSERT INTO `django_admin_log` VALUES ('391', '2017-04-29 00:58:44', '7', 'Cofoe Commode Chair (ZC019)', '1', '', '13', '1');
INSERT INTO `django_admin_log` VALUES ('392', '2017-04-29 01:18:36', '1', 'banner1', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('393', '2017-04-29 01:18:51', '2', 'banner2', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('394', '2017-04-29 01:19:09', '3', 'banner3', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('395', '2017-04-29 09:22:12', '4', 'Cuppings', '1', '', '12', '1');
INSERT INTO `django_admin_log` VALUES ('396', '2017-04-29 09:22:18', '8', 'Cofoe Cuppings (KFA-12)', '1', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('397', '2017-04-29 09:22:37', '8', 'Cofoe Cuppings (KFA-12)', '2', '已修改 default 。 已添加 product image \"Cofoe Cuppings (KFA-12)\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('398', '2017-04-29 09:22:49', '8', 'Cofoe Cuppings (KFA-12)', '2', '已变更 title，sale_price 和 inventory for variation \"KFA-12\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('399', '2017-04-29 09:23:31', '9', 'Cofoe Cuppings (KFA-6)', '1', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('400', '2017-04-29 09:23:49', '9', 'Cofoe Cuppings (KFA-6)', '2', '已变更 title for variation \"KFA-6\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('401', '2017-04-29 09:24:35', '5', 'Thermometer', '1', '', '12', '1');
INSERT INTO `django_admin_log` VALUES ('402', '2017-04-29 09:24:38', '10', 'Thermometer', '1', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('403', '2017-04-29 09:24:51', '10', 'Thermometer', '2', '已修改 default 。 已添加 product image \"Thermometer\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('404', '2017-04-29 09:25:06', '10', 'ThermometerCofoe Non-Contact Digital Infrared Thermometer Ear Temperatu', '2', '已修改 title 。 已变更 title for variation \"Cofoe Non-Contact Digital Infrared Thermometer Ear Temperatu\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('405', '2017-04-29 09:25:42', '11', 'Cofoe Digital Thermometer (TM-3002)', '1', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('406', '2017-04-29 09:26:11', '11', 'Cofoe Digital Thermometer (TM-3002)', '2', '已变更 title，sale_price 和 inventory for variation \"TM-3002\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('407', '2017-04-29 10:02:58', '6', 'Walkers', '1', '', '12', '1');
INSERT INTO `django_admin_log` VALUES ('408', '2017-04-29 14:45:40', '9', 'Cofoe Cuppings (KFA-6)', '2', '已修改 description 。', '9', '1');
INSERT INTO `django_admin_log` VALUES ('409', '2017-04-29 14:47:51', '9', 'Cofoe Cuppings (KFA-6)', '2', '已修改 description 。', '9', '1');
INSERT INTO `django_admin_log` VALUES ('410', '2017-04-29 14:57:11', '9', 'Cofoe Cuppings (KFA-6)', '2', '已修改 description 。', '9', '1');
INSERT INTO `django_admin_log` VALUES ('411', '2017-04-30 01:00:49', '7', 'Cofoe Commode Chair (ZC067)', '2', '已添加 product image \"Cofoe Commode Chair (ZC067)\". 已添加 product image \"Cofoe Commode Chair (ZC067)\". 已添加 product image \"Cofoe Commode Chair (ZC067)\". 已添加 product image \"Cofoe Commode Chair (ZC067)\". 已添加 product image \"Cofoe Commode Chair (ZC067)\". 已添加 product image \"Cofoe Commode Chair (ZC067)\". 已添加 product image \"Cofoe Commode Chair (ZC067)\". 已添加 product image \"Cofoe Commode Chair (ZC067)\". 已添加 product image \"Cofoe Commode Chair (ZC067)\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('412', '2017-04-30 04:47:01', '1', 'Article object', '1', '', '29', '1');
INSERT INTO `django_admin_log` VALUES ('413', '2017-04-30 05:04:34', '1', 'Article object', '2', '已修改 content 。', '29', '1');
INSERT INTO `django_admin_log` VALUES ('414', '2017-04-30 05:06:04', '1', 'Article object', '2', '已修改 content 。', '29', '1');
INSERT INTO `django_admin_log` VALUES ('415', '2017-04-30 05:51:19', '2', 'Article object', '1', '', '29', '1');
INSERT INTO `django_admin_log` VALUES ('416', '2017-04-30 07:23:09', '3', 'Article object', '1', '', '29', '1');
INSERT INTO `django_admin_log` VALUES ('417', '2017-04-30 09:56:48', '12', 'iPhone', '1', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('418', '2017-04-30 09:57:24', '12', 'iPhone', '2', '已修改 description 。 已变更 title，sale_price 和 inventory for variation \"iPhone7\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('419', '2017-04-30 09:57:37', '7', 'Cofoe Commode Chair (ZC019)', '3', '', '13', '1');
INSERT INTO `django_admin_log` VALUES ('420', '2017-04-30 09:57:38', '6', 'Cofoe Commode Chair (ZC065)', '3', '', '13', '1');
INSERT INTO `django_admin_log` VALUES ('421', '2017-04-30 09:57:38', '5', 'Cofoe Commode Chair (ZC067)', '3', '', '13', '1');
INSERT INTO `django_admin_log` VALUES ('422', '2017-04-30 09:57:58', '8', 'iPhone', '1', '', '13', '1');
INSERT INTO `django_admin_log` VALUES ('423', '2017-04-30 10:38:52', '10', 'ThermometerCofoe Non-Contact Digital Infrared Thermometer Ear Temperatu', '2', '已变更 image for product image \"ThermometerCofoe Non-Contact Digital Infrared Thermometer Ear Temperatu\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('424', '2017-04-30 10:39:31', '12', 'iPhone', '2', '已变更 image for product image \"iPhone\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('425', '2017-04-30 10:39:56', '11', 'Cofoe Digital Thermometer (TM-3002)', '2', '已变更 image for product image \"Cofoe Digital Thermometer (TM-3002)\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('426', '2017-04-30 10:40:56', '9', 'Cofoe Cuppings (KFA-6)', '2', '已变更 image for product image \"Cofoe Cuppings (KFA-6)\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('427', '2017-04-30 10:41:16', '8', 'Cofoe Cuppings (KFA-12)', '2', '已变更 image for product image \"Cofoe Cuppings (KFA-12)\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('428', '2017-04-30 10:44:05', '7', 'Cofoe Commode Chair (ZC067)', '2', '已变更 image for product image \"Cofoe Commode Chair (ZC067)\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('429', '2017-04-30 10:45:13', '7', 'Cofoe Commode Chair (ZC067)', '2', '已变更 image for product image \"Cofoe Commode Chair (ZC067)\". 已变更 image for product image \"Cofoe Commode Chair (ZC067)\". 已变更 image for product image \"Cofoe Commode Chair (ZC067)\". 已变更 image for product image \"Cofoe Commode Chair (ZC067)\". 已变更 image for product image \"Cofoe Commode Chair (ZC067)\". 已变更 image for product image \"Cofoe Commode Chair (ZC067)\". 已变更 image for product image \"Cofoe Commode Chair (ZC067)\". 已变更 image for product image \"Cofoe Commode Chair (ZC067)\". 已变更 image for product image \"Cofoe Commode Chair (ZC067)\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('430', '2017-04-30 10:52:52', '7', 'Cofoe Commode Chair (ZC067)', '2', '已变更 image for product image \"Cofoe Commode Chair (ZC067)\". 已变更 image for product image \"Cofoe Commode Chair (ZC067)\". 已变更 image for product image \"Cofoe Commode Chair (ZC067)\". 已变更 image for product image \"Cofoe Commode Chair (ZC067)\". 已变更 image for product image \"Cofoe Commode Chair (ZC067)\". 已变更 image for product image \"Cofoe Commode Chair (ZC067)\". 已变更 image for product image \"Cofoe Commode Chair (ZC067)\". 已变更 image for product image \"Cofoe Commode Chair (ZC067)\". 已变更 image for product image \"Cofoe Commode Chair (ZC067)\". 已变更 image for product image \"Cofoe Commode Chair (ZC067)\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('431', '2017-04-30 10:54:14', '4', 'Cofoe Commode Chair (ZC065)', '2', '已变更 image for product image \"Cofoe Commode Chair (ZC065)\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('432', '2017-04-30 10:54:29', '6', 'Cofoe Commode Chair (ZC019)', '2', '已变更 image for product image \"Cofoe Commode Chair (ZC019)\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('433', '2017-04-30 10:54:40', '5', 'Cofoe Commode Chair (ZC018)', '2', '已变更 image for product image \"Cofoe Commode Chair (ZC018)\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('434', '2017-04-30 11:00:28', '10', 'ThermometerCofoe Non-Contact Digital Infrared Thermometer Ear Temperatu', '2', '已变更 image for product image \"ThermometerCofoe Non-Contact Digital Infrared Thermometer Ear Temperatu\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('435', '2017-04-30 11:00:32', '10', 'ThermometerCofoe Non-Contact Digital Infrared Thermometer Ear Temperatu', '2', '没有字段被修改。', '9', '1');
INSERT INTO `django_admin_log` VALUES ('436', '2017-04-30 11:00:45', '11', 'Cofoe Digital Thermometer (TM-3002)', '2', '已变更 image for product image \"Cofoe Digital Thermometer (TM-3002)\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('437', '2017-04-30 11:01:16', '10', 'ThermometerCofoe Non-Contact Digital Infrared Thermometer Ear Temperatu', '2', '没有字段被修改。', '9', '1');
INSERT INTO `django_admin_log` VALUES ('438', '2017-04-30 11:02:00', '9', 'Cofoe Cuppings (KFA-6)', '2', '已变更 image for product image \"Cofoe Cuppings (KFA-6)\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('439', '2017-04-30 11:02:08', '8', 'Cofoe Cuppings (KFA-12)', '2', '已变更 image for product image \"Cofoe Cuppings (KFA-12)\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('440', '2017-04-30 11:03:29', '12', 'iPhone', '2', '已变更 image for product image \"iPhone\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('441', '2017-04-30 11:04:09', '8', 'iPhone', '2', '已修改 image 。', '13', '1');
INSERT INTO `django_admin_log` VALUES ('442', '2017-04-30 13:33:51', '10', 'ThermometerCofoe Non-Contact Digital Infrared Thermometer Ear Temperatu', '2', '已变更 image for product image \"ThermometerCofoe Non-Contact Digital Infrared Thermometer Ear Temperatu\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('443', '2017-04-30 13:39:45', '9', 'Cofoe Cuppings (KFA-6)', '2', '已变更 image for product image \"Cofoe Cuppings (KFA-6)\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('444', '2017-04-30 13:40:19', '8', 'Cofoe Cuppings (KFA-12)', '2', '已变更 image for product image \"Cofoe Cuppings (KFA-12)\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('445', '2017-04-30 13:40:21', '8', 'Cofoe Cuppings (KFA-12)', '2', '没有字段被修改。', '9', '1');
INSERT INTO `django_admin_log` VALUES ('446', '2017-04-30 13:47:20', '10', 'ThermometerCofoe Non-Contact Digital Infrared Thermometer Ear Temperatu', '2', '已变更 image for product image \"ThermometerCofoe Non-Contact Digital Infrared Thermometer Ear Temperatu\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('447', '2017-04-30 13:47:49', '11', 'Cofoe Digital Thermometer (TM-3002)', '2', '已变更 image for product image \"Cofoe Digital Thermometer (TM-3002)\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('448', '2017-04-30 13:47:57', '11', 'Cofoe Digital Thermometer (TM-3002)', '2', '没有字段被修改。', '9', '1');
INSERT INTO `django_admin_log` VALUES ('449', '2017-04-30 13:49:35', '11', 'Cofoe Digital Thermometer (TM-3002)', '2', '已变更 image for product image \"Cofoe Digital Thermometer (TM-3002)\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('450', '2017-04-30 13:49:58', '10', 'ThermometerCofoe Non-Contact Digital Infrared Thermometer Ear Temperatu', '2', '已变更 image for product image \"ThermometerCofoe Non-Contact Digital Infrared Thermometer Ear Temperatu\".', '9', '1');
INSERT INTO `django_admin_log` VALUES ('529', '2017-07-09 13:20:17', '1', 'bhe001', '2', '已修改 username 和 last_login 。', '30', '1');
INSERT INTO `django_admin_log` VALUES ('530', '2017-07-15 03:20:41', '102', '+8613410010002 - 047558', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('531', '2017-07-15 03:20:41', '101', '+8613420010002 - 566869', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('532', '2017-07-15 03:20:41', '100', '+8613420010002 - 194679', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('533', '2017-07-15 03:20:41', '99', '+8613420010002 - 704752', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('534', '2017-07-15 03:20:41', '98', '+8613401010002 - 064761', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('535', '2017-07-15 03:20:41', '97', '+8613245678901 - 379868', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('536', '2017-07-15 03:20:41', '96', '+8613456789013 - 455388', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('537', '2017-07-15 03:20:41', '95', '+8613456789012 - 323278', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('538', '2017-07-15 03:20:41', '94', '+NoneNone - 991293', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('539', '2017-07-15 03:20:41', '93', '+8613400010075 - 237967', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('540', '2017-07-15 03:20:41', '92', '+8613400010065 - 693865', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('541', '2017-07-15 03:20:41', '91', '+8613400010055 - 924271', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('542', '2017-07-15 03:20:41', '90', '+8613400010045 - 407829', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('543', '2017-07-15 03:20:41', '89', '+8613400010035 - 881931', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('544', '2017-07-15 03:20:41', '88', '+8613400010025 - 151278', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('545', '2017-07-15 03:20:41', '87', '+8613400010015 - 863221', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('546', '2017-07-15 03:20:41', '86', '+8613113331123 - 415532', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('547', '2017-07-15 03:20:41', '85', '+8613113331123 - 012246', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('548', '2017-07-15 03:20:41', '84', '+8613400010006 - 877986', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('549', '2017-07-15 03:20:41', '83', '+8613400010006 - 713265', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('550', '2017-07-15 03:20:41', '82', '+8613400010006 - 047491', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('551', '2017-07-15 03:20:41', '81', '+8613400010006 - 493595', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('552', '2017-07-15 03:20:42', '80', '+8613400010002 - 869952', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('553', '2017-07-15 03:20:42', '79', '+8613567890012 - 264585', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('554', '2017-07-15 03:20:42', '78', '+8613567890012 - 224241', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('555', '2017-07-15 03:20:42', '77', '+8613400010005 - 682558', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('556', '2017-07-15 03:20:42', '76', '+8613400010005 - 506589', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('557', '2017-07-15 03:20:42', '75', '+8613400010004 - 831449', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('558', '2017-07-15 03:20:42', '74', '+8613400010003 - 022539', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('559', '2017-07-15 03:20:42', '73', '+8613400000007 - 854625', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('560', '2017-07-15 03:20:42', '72', '+8613400000009 - 367436', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('561', '2017-07-15 03:20:42', '71', '+8613400000001 - 432858', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('562', '2017-07-15 03:20:42', '70', '+1013500010004 - 639086', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('563', '2017-07-15 03:20:42', '69', '+8613400010004 - 558232', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('564', '2017-07-15 03:20:42', '68', '+8613400010003 - 930711', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('565', '2017-07-15 03:20:42', '67', '+8613400010002 - 079124', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('566', '2017-07-15 03:20:42', '66', '+8613400010002 - 081129', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('567', '2017-07-15 03:20:42', '65', '+8613400010002 - 945576', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('568', '2017-07-15 03:20:42', '64', '+8613400010002 - 879627', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('569', '2017-07-15 03:20:42', '63', '+8613400010002 - 361225', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('570', '2017-07-15 03:20:42', '62', '+8613400010002 - 509162', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('571', '2017-07-15 03:20:42', '61', '+8613400010002 - 410531', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('572', '2017-07-15 03:20:42', '60', '+8613400010002 - 682274', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('573', '2017-07-15 03:20:42', '59', '+8613400010002 - 236640', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('574', '2017-07-15 03:20:42', '58', '+8613400010002 - 505604', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('575', '2017-07-15 03:20:42', '57', '+8613400010002 - 428385', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('576', '2017-07-15 03:20:42', '56', '+8613400010002 - 529587', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('577', '2017-07-15 03:20:42', '55', '+8613400010002 - 204382', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('578', '2017-07-15 03:20:42', '54', '+8613400010002 - 735926', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('579', '2017-07-15 03:20:42', '53', '+8613400010002 - 601842', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('580', '2017-07-15 03:20:42', '52', '+8613400010002 - 559967', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('581', '2017-07-15 03:20:42', '51', '+8613400010002 - 784258', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('582', '2017-07-15 03:20:42', '50', '+8613400010002 - 459173', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('583', '2017-07-15 03:20:42', '49', '+8613400010002 - 102416', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('584', '2017-07-15 03:20:42', '48', '+NoneNone - 660829', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('585', '2017-07-15 03:20:42', '47', '+8613400010002 - 574500', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('586', '2017-07-15 03:20:42', '46', '+8613400010002 - 900785', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('587', '2017-07-15 03:20:42', '45', '+8613400010002 - 529053', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('588', '2017-07-15 03:20:42', '44', '+8613400010002 - 882215', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('589', '2017-07-15 03:20:42', '43', '+8613400010002 - 963878', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('590', '2017-07-15 03:20:42', '42', '+8613400010002 - 395515', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('591', '2017-07-15 03:20:43', '41', '+8613400010002 - 524375', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('592', '2017-07-15 03:20:43', '40', '+8613400010002 - 630414', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('593', '2017-07-15 03:20:43', '39', '+8613400010002 - 759619', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('594', '2017-07-15 03:20:43', '38', '+8613400010002 - 610854', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('595', '2017-07-15 03:20:43', '37', '+8613400010002 - 460258', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('596', '2017-07-15 03:20:43', '36', '+8613400010002 - 296371', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('597', '2017-07-15 03:20:43', '35', '+8613400010002 - 921944', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('598', '2017-07-15 03:20:43', '34', '+8613400010002 - 844001', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('599', '2017-07-15 03:20:43', '33', '+8613400010002 - 091864', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('600', '2017-07-15 03:20:43', '32', '+8613400010002 - 955167', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('601', '2017-07-15 03:20:43', '31', '+8613400010002 - 010232', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('602', '2017-07-15 03:20:43', '30', '+8613400010002 - 379713', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('603', '2017-07-15 03:20:43', '29', '+NoneNone - 912697', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('604', '2017-07-15 03:20:43', '28', '+8613400010002 - 337022', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('605', '2017-07-15 03:20:43', '27', '+8613400010002 - 430165', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('606', '2017-07-15 03:20:43', '26', '+8613400010002 - 209097', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('607', '2017-07-15 03:20:43', '25', '+8613400010002 - 958822', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('608', '2017-07-15 03:20:43', '24', '+8613400010002 - 723376', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('609', '2017-07-15 03:20:43', '23', '+8613400010002 - 745283', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('610', '2017-07-15 03:20:43', '22', '+8613400010002 - 257782', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('611', '2017-07-15 03:20:43', '21', '+8613400010002 - 550184', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('612', '2017-07-15 03:20:43', '20', '+8613400010002 - 803862', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('613', '2017-07-15 03:20:43', '19', '+8613400010002 - 181433', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('614', '2017-07-15 03:20:43', '18', '+8613400010002 - 906249', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('615', '2017-07-15 03:20:43', '17', '+8613400010002 - 886319', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('616', '2017-07-15 03:20:43', '16', '+8613400010002 - 819816', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('617', '2017-07-15 03:20:43', '15', '+8613400010002 - 418159', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('618', '2017-07-15 03:20:43', '14', '+8613400010002 - 007217', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('619', '2017-07-15 03:20:43', '13', '+8613400010002 - 188891', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('620', '2017-07-15 03:20:43', '12', '+8613400010002 - 175197', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('621', '2017-07-15 03:20:43', '11', '+8613400010002 - 863116', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('622', '2017-07-15 03:20:43', '10', '+8613400010002 - 330998', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('623', '2017-07-15 03:20:43', '9', '+8613400010002 - 746787', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('624', '2017-07-15 03:20:43', '8', '+8613400010002 - 855412', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('625', '2017-07-15 03:20:43', '7', '+8613400010002 - 899527', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('626', '2017-07-15 03:20:43', '6', '+8613400010002 - 829820', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('627', '2017-07-15 03:20:43', '5', '+8613400010002 - 347789', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('628', '2017-07-15 03:20:43', '4', '+8613400010002 - 616441', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('629', '2017-07-15 03:20:43', '3', '+8613400010002 - 132406', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('630', '2017-07-15 03:20:49', '2', '+8613400010002 - 037923', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('631', '2017-07-15 03:20:49', '1', '+8613400010002 - 183546', '3', '', '32', '1');
INSERT INTO `django_admin_log` VALUES ('632', '2017-07-15 03:31:51', '24', '+8613500192123', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('633', '2017-07-15 03:31:51', '23', '+8613410010002', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('634', '2017-07-15 03:31:51', '22', '+8613401010002', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('635', '2017-07-15 03:31:51', '21', '+8613245678901', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('636', '2017-07-15 03:31:51', '20', '+8613456789013', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('637', '2017-07-15 03:31:51', '19', '+8613456789012', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('638', '2017-07-15 03:31:51', '18', '+8613400010075', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('639', '2017-07-15 03:31:51', '17', '+8613400010065', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('640', '2017-07-15 03:31:51', '16', '+8613400010055', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('641', '2017-07-15 03:31:51', '15', '+8613400010045', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('642', '2017-07-15 03:31:51', '14', '+8613400010035', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('643', '2017-07-15 03:31:51', '13', '+8613400010025', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('644', '2017-07-15 03:31:51', '12', '+8613400010015', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('645', '2017-07-15 03:31:51', '11', '+8613113331123', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('646', '2017-07-15 03:31:51', '10', '+8613400010006', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('647', '2017-07-15 03:31:51', '9', '+8613400010005', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('648', '2017-07-15 03:31:51', '8', '+8613400000007', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('649', '2017-07-15 03:31:51', '7', '+8613400000009', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('650', '2017-07-15 03:31:51', '6', '+8613400000001', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('651', '2017-07-15 03:31:51', '5', '+8613400010004', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('652', '2017-07-15 03:31:51', '4', '+8613400010003', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('653', '2017-07-15 03:31:51', '3', '+8613400010002', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('654', '2017-07-15 03:31:51', '2', '', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('655', '2017-07-15 04:33:35', '2', 'hebinn', '2', '已修改 user 。', '31', '1');
INSERT INTO `django_admin_log` VALUES ('656', '2017-07-15 04:37:02', '2', 'hebinn', '2', '已修改 user 。', '31', '1');
INSERT INTO `django_admin_log` VALUES ('657', '2017-07-15 04:48:35', '2', 'hebinn', '2', '没有字段被修改。', '31', '1');
INSERT INTO `django_admin_log` VALUES ('658', '2017-07-15 05:00:32', '2', 'hebinn', '2', '已修改 user 。', '31', '1');
INSERT INTO `django_admin_log` VALUES ('659', '2017-07-15 05:53:19', '41', '+8613900000050', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('660', '2017-07-15 05:53:19', '40', '+8613900000040', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('661', '2017-07-15 05:53:19', '39', '+8613900000030', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('662', '2017-07-15 05:53:19', '38', '+8613900000021', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('663', '2017-07-15 05:53:19', '37', '+8613900000011', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('664', '2017-07-15 05:53:19', '36', '+8613800000009', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('665', '2017-07-15 05:53:19', '35', '+8613800000008', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('666', '2017-07-15 05:53:19', '34', '+8613800000007', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('667', '2017-07-15 05:53:19', '33', '+8613800000005', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('668', '2017-07-15 05:53:20', '32', '+8613800000004', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('669', '2017-07-15 05:53:20', '31', '+8613900000003', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('670', '2017-07-15 05:53:20', '30', '+8613900000002', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('671', '2017-07-15 05:53:20', '29', '+8613900000001', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('672', '2017-07-15 05:53:20', '28', '+8613900000000', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('673', '2017-07-15 05:53:20', '27', '+8613800000000', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('674', '2017-07-15 05:53:20', '26', '+8613700000000', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('675', '2017-07-15 05:53:20', '25', '+8613600000000', '3', '', '30', '1');
INSERT INTO `django_admin_log` VALUES ('676', '2017-07-15 06:50:13', '3', 'hebinn', '3', '', '31', '1');
INSERT INTO `django_admin_log` VALUES ('677', '2017-07-15 06:51:15', '42', '13500000001', '2', '已修改 username，is_active 和 last_login 。', '30', '1');
INSERT INTO `django_admin_log` VALUES ('678', '2017-07-16 00:40:46', '43', '13600000000', '2', '已修改 username，is_staff 和 last_login 。', '30', '1');
INSERT INTO `django_admin_log` VALUES ('679', '2017-08-05 08:52:57', '323', 'csdong: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('680', '2017-08-05 08:52:57', '326', 'Bin3 He2: 12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('681', '2017-08-05 08:52:57', '331', 'Bin3 He2: dasd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('682', '2017-08-05 08:52:57', '330', 'Bin3 He2: 121211111111111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('683', '2017-08-05 08:52:57', '332', 'Bin3 He2: 1111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('684', '2017-08-05 08:52:57', '333', 'Bin3 He2: 1212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('685', '2017-08-05 08:52:57', '334', 'Bin3 He2: 1231313...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('686', '2017-08-05 08:52:57', '335', 'Bin3 He2: 12121212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('687', '2017-08-05 08:52:57', '336', 'Bin3 He2: 1212121212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('688', '2017-08-05 08:52:57', '337', 'Bin3 He2: 12121212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('689', '2017-08-05 08:52:57', '324', 'csdong: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('690', '2017-08-05 08:52:57', '325', 'Bin3 He2: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('691', '2017-08-05 08:52:57', '340', 'Bin3 He2: 1112fdfd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('692', '2017-08-05 08:52:57', '341', 'Bin3 He2: 1112fdfd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('693', '2017-08-05 08:52:57', '342', 'Bin3 He2: fadfsafsd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('694', '2017-08-05 08:52:57', '343', 'Bin3 He2: faffffffffffff...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('695', '2017-08-05 08:52:57', '327', 'csdong: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('696', '2017-08-05 08:52:57', '328', 'csdong: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('697', '2017-08-05 08:52:58', '329', 'csdong: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('698', '2017-08-05 08:52:58', '338', 'csdong: 12121211111111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('699', '2017-08-05 08:52:58', '339', '121: 1212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('700', '2017-08-05 08:52:58', '344', 'example: test...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('701', '2017-08-05 08:52:58', '345', 'post: post...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('702', '2017-08-05 08:52:58', '346', '+8613500000000: fdasfsafa...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('703', '2017-08-05 08:52:58', '347', '+8613500000000: fdasfsafa...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('704', '2017-08-05 08:52:58', '348', '+8613500000000: dafs...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('705', '2017-08-05 08:52:58', '349', '+8613500000000: fsfsdfs...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('706', '2017-08-05 08:52:58', '350', '+8613500000000: haha...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('707', '2017-08-05 08:52:58', '351', '+8613500000000: haha...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('708', '2017-08-05 08:52:58', '352', 'post: 12thisdfsf...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('709', '2017-08-05 08:52:58', '353', 'post: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('710', '2017-08-05 08:52:58', '354', '+8613500000000: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('711', '2017-08-05 08:52:58', '355', '+8613500000000: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('712', '2017-08-05 08:52:58', '356', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('713', '2017-08-05 08:52:58', '357', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('714', '2017-08-05 08:52:58', '358', '+8613500000000: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('715', '2017-08-05 08:52:58', '359', '+8613500000000: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('716', '2017-08-05 08:52:58', '360', '+8613500000000: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('717', '2017-08-05 08:52:58', '361', '+8613500000000: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('718', '2017-08-05 08:52:58', '362', '+8613500000000: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('719', '2017-08-05 08:52:58', '363', '+8613500000000: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('720', '2017-08-05 08:52:58', '364', '+8613500000000: 10...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('721', '2017-08-05 08:52:58', '365', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('722', '2017-08-05 08:52:58', '366', '+8613500000000: 12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('723', '2017-08-05 08:52:58', '367', '+8613500000000: 13...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('724', '2017-08-05 08:52:58', '372', '+8613500000000: 16...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('725', '2017-08-05 08:52:58', '373', '+8613500000000: 16...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('726', '2017-08-05 08:52:58', '374', '+8613500000000: 17...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('727', '2017-08-05 08:52:58', '375', '+8613500000000: 18...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('728', '2017-08-05 08:52:58', '376', '+8613500000000: 19...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('729', '2017-08-05 08:52:58', '368', '+8613500000000: 14...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('730', '2017-08-05 08:52:58', '370', '+8613500000000: 15...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('731', '2017-08-05 08:52:58', '371', '+8613500000000: 15...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('732', '2017-08-05 08:52:59', '377', '+8613500000000: 15...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('733', '2017-08-05 08:52:59', '378', '+8613500000000: 15...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('734', '2017-08-05 08:52:59', '379', 'post: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('735', '2017-08-05 08:52:59', '380', '+8613500000000: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('736', '2017-08-05 08:52:59', '381', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('737', '2017-08-05 08:52:59', '382', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('738', '2017-08-05 08:52:59', '383', '+8613500000000: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('739', '2017-08-05 08:52:59', '393', '+8613500000000: 14...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('740', '2017-08-05 08:52:59', '394', '+8613500000000: 15...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('741', '2017-08-05 08:52:59', '384', '+8613500000000: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('742', '2017-08-05 08:52:59', '385', '+8613500000000: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('743', '2017-08-05 08:52:59', '386', '+8613500000000: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('744', '2017-08-05 08:52:59', '387', '+8613500000000: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('745', '2017-08-05 08:52:59', '388', '+8613500000000: 10...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('746', '2017-08-05 08:52:59', '389', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('747', '2017-08-05 08:52:59', '390', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('748', '2017-08-05 08:52:59', '391', '+8613500000000: 12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('749', '2017-08-05 08:52:59', '392', '+8613500000000: 13...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('750', '2017-08-05 08:52:59', '395', '+8613500000000: 21...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('751', '2017-08-05 08:52:59', '396', '+8613500000000: 21...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('752', '2017-08-05 08:52:59', '397', '+8613500000000: 22...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('753', '2017-08-05 08:52:59', '398', '+8613500000000: 23...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('754', '2017-08-05 08:52:59', '399', '+8613500000000: 111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('755', '2017-08-05 08:52:59', '400', '+8613500000000: 111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('756', '2017-08-05 08:52:59', '401', '+8613500000000: 121...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('757', '2017-08-05 08:52:59', '402', '+8613500000000: 121...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('758', '2017-08-05 08:52:59', '403', '+8613500000000: 122...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('759', '2017-08-05 08:52:59', '404', '+8613500000000: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('760', '2017-08-05 08:52:59', '405', '123: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('761', '2017-08-05 08:52:59', '413', '+8613500000000: 204...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('762', '2017-08-05 08:52:59', '406', '124: 124...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('763', '2017-08-05 08:52:59', '407', 'post: 126...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('764', '2017-08-05 08:52:59', '408', '+8613500000000: 200...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('765', '2017-08-05 08:52:59', '409', '+8613500000000: 200...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('766', '2017-08-05 08:52:59', '410', '+8613500000000: 201...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('767', '2017-08-05 08:52:59', '411', '+8613500000000: 202...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('768', '2017-08-05 08:53:00', '412', '+8613500000000: 203...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('769', '2017-08-05 08:53:00', '414', '+8613500000000: 245...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('770', '2017-08-05 08:53:00', '415', '+8613500000000: 333333333...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('771', '2017-08-05 08:53:00', '416', '+8613500000000: 333333333...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('772', '2017-08-05 08:53:00', '417', '+8613500000000: 44444444...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('773', '2017-08-05 08:53:00', '418', 'post: 1111111111111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('774', '2017-08-05 08:53:00', '419', '+8613500000000: 222222222222...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('775', '2017-08-05 08:53:00', '420', '+8613500000000: dafsdfsdfsd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('776', '2017-08-05 08:53:00', '422', '+8613500000000: sdfsdfsdfsd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('777', '2017-08-05 08:53:00', '424', '+8613500000000: wwwwwwwwwwwwww...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('778', '2017-08-05 08:53:00', '427', '+8613500000000: 1213...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('779', '2017-08-05 08:53:08', '428', '+8613500000000: qqqqq...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('780', '2017-08-05 08:53:08', '429', '+8613500000000: tttttt...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('781', '2017-08-05 08:53:08', '430', '+8613500000000: zzzz...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('782', '2017-08-05 08:53:08', '431', '+8613500000000: qqq...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('783', '2017-08-05 08:53:08', '433', '+8613500000000: sssss...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('784', '2017-08-05 08:53:08', '434', '+8613500000000: vvv...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('785', '2017-08-05 08:53:08', '435', '+8613500000000: bbbb...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('786', '2017-08-05 08:53:08', '436', '+8613500000000: nnnn...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('787', '2017-08-05 08:53:08', '438', '+8613500000000: mmmm...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('788', '2017-08-05 08:53:08', '439', '+8613500000000: aaaaa...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('789', '2017-08-05 08:53:08', '440', '+8613500000000: vvvv...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('790', '2017-08-05 08:53:08', '442', '+8613500000000: zzz...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('791', '2017-08-05 08:53:08', '443', '+8613500000000: jjjj...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('792', '2017-08-05 08:53:08', '444', '+8613500000000: tttt...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('793', '2017-08-05 08:53:08', '445', '+8613500000000: sdsafasf...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('794', '2017-08-05 08:53:08', '447', '+8613500000000: ccccc...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('795', '2017-08-05 08:53:09', '449', '+8613500000000: xxx...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('796', '2017-08-05 08:53:09', '450', '+8613500000000: mmmmmmmmmm...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('797', '2017-08-05 08:53:09', '452', '+8613500000000: mmmmmm...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('798', '2017-08-05 08:53:09', '453', '+8613500000000: qwqwqwqwqw...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('799', '2017-08-05 08:53:09', '454', '+8613500000000: llllllllllllllllllllllllllllllllllllllllllllllllll...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('800', '2017-08-05 08:53:09', '456', '+8613500000000: 5555555555555555555555555555555555555555555555555...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('801', '2017-08-05 08:53:09', '457', '+8613500000000: 5555555555555555555555...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('802', '2017-08-05 08:53:09', '458', '+8613500000000: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('803', '2017-08-05 08:53:09', '460', '+8613500000000: 11111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('804', '2017-08-05 08:53:09', '462', '+8613500000000: sdsdsd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('805', '2017-08-05 08:53:09', '464', '+8613500000000: 121212121...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('806', '2017-08-05 08:53:09', '468', '+8613500000000: 12121212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('807', '2017-08-05 08:53:09', '469', '+8613500000000: 12121212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('808', '2017-08-05 08:53:09', '466', '+8613500000000: 1212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('809', '2017-08-05 08:53:09', '470', '+8613500000000: ,,,,,,,,,,,,,,,,...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('810', '2017-08-05 13:43:57', '472', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('811', '2017-08-05 13:43:57', '474', '+8613500000000: 22...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('812', '2017-08-05 13:43:57', '475', '+8613500000000: 22...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('813', '2017-08-05 13:43:57', '478', '+8613500000000: 1212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('814', '2017-08-05 13:43:57', '479', '+8613500000000: 1212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('815', '2017-08-05 13:43:57', '480', '+8613500000000: 121212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('816', '2017-08-05 13:43:57', '481', '+8613500000000: 121212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('817', '2017-08-05 13:43:57', '482', '+8613500000000: 12121...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('818', '2017-08-05 13:43:57', '483', '+8613500000000: 12121...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('819', '2017-08-05 13:43:57', '484', '+8613500000000: 111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('820', '2017-08-05 13:43:57', '485', '+8613500000000: 111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('821', '2017-08-05 13:43:57', '486', '+8613500000000: 112...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('822', '2017-08-05 13:43:57', '487', '+8613500000000: 112...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('823', '2017-08-05 13:43:57', '490', '+8613500000000: 1111111111111111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('824', '2017-08-05 13:43:58', '491', '+8613500000000: 1111111111111111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('825', '2017-08-05 13:43:58', '476', '+8613500000000: 33...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('826', '2017-08-05 13:43:58', '488', '111: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('827', '2017-08-05 13:43:58', '489', '+8613500000000: 1234...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('828', '2017-08-05 13:43:58', '492', '1: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('829', '2017-08-05 13:43:58', '493', '+8613500000000: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('830', '2017-08-05 13:43:58', '494', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('831', '2017-08-05 13:43:58', '495', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('832', '2017-08-05 13:43:58', '502', '+8613500000000: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('833', '2017-08-05 13:43:58', '503', '+8613500000000: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('834', '2017-08-05 13:43:58', '504', '+8613500000000: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('835', '2017-08-05 13:43:58', '505', '+8613500000000: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('836', '2017-08-05 13:43:58', '506', '+8613500000000: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('837', '2017-08-05 13:43:58', '507', '+8613500000000: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('838', '2017-08-05 13:43:58', '500', '+8613500000000: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('839', '2017-08-05 13:43:58', '501', '+8613500000000: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('840', '2017-08-05 13:43:58', '496', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('841', '2017-08-05 13:43:58', '497', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('842', '2017-08-05 13:43:58', '498', '+8613500000000: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('843', '2017-08-05 13:43:58', '499', '+8613500000000: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('844', '2017-08-05 16:10:59', '508', 'post: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('845', '2017-08-05 16:10:59', '509', '+8613500000000: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('846', '2017-08-05 16:10:59', '510', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('847', '2017-08-05 16:10:59', '511', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('848', '2017-08-05 16:10:59', '512', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('849', '2017-08-05 16:10:59', '513', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('850', '2017-08-05 16:10:59', '514', '+8613500000000: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('851', '2017-08-05 16:10:59', '515', '+8613500000000: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('852', '2017-08-05 16:10:59', '516', '+8613500000000: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('853', '2017-08-05 16:10:59', '517', '+8613500000000: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('854', '2017-08-05 16:10:59', '518', '+8613500000000: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('855', '2017-08-05 16:10:59', '519', '+8613500000000: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('856', '2017-08-05 16:10:59', '520', '+8613500000000: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('857', '2017-08-05 16:10:59', '521', '+8613500000000: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('858', '2017-08-05 16:10:59', '522', '+8613500000000: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('859', '2017-08-05 16:10:59', '523', '+8613500000000: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('860', '2017-08-05 16:10:59', '524', '+8613500000000: 10...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('861', '2017-08-05 16:10:59', '525', '+8613500000000: 10...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('862', '2017-08-05 16:11:00', '526', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('863', '2017-08-05 16:11:00', '527', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('864', '2017-08-05 16:11:00', '528', '+8613500000000: 12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('865', '2017-08-05 16:11:00', '529', '+8613500000000: 12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('866', '2017-08-05 16:11:00', '530', '+8613500000000: 13...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('867', '2017-08-05 16:11:00', '531', '+8613500000000: 13...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('868', '2017-08-05 16:11:00', '532', '+8613500000000: 14...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('869', '2017-08-05 16:11:00', '533', '+8613500000000: 14...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('870', '2017-08-05 16:11:00', '534', '+8613500000000: 15...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('871', '2017-08-05 16:11:00', '535', '+8613500000000: 15...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('872', '2017-08-05 16:11:00', '536', '+8613500000000: 16...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('873', '2017-08-05 16:11:00', '537', '+8613500000000: 16...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('874', '2017-08-05 16:11:00', '538', '+8613500000000: 17...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('875', '2017-08-05 16:11:00', '539', '+8613500000000: 17...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('876', '2017-08-05 16:11:00', '540', '+8613500000000: 18...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('877', '2017-08-05 16:11:00', '541', '+8613500000000: 18...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('878', '2017-08-05 16:11:00', '542', '+8613500000000: 19...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('879', '2017-08-05 16:11:00', '543', '+8613500000000: 19...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('880', '2017-08-05 16:11:00', '544', '+8613500000000: 20...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('881', '2017-08-05 16:11:00', '545', '+8613500000000: 20...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('882', '2017-08-05 16:11:00', '553', '+8613500000000: 24...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('883', '2017-08-05 16:11:00', '554', '+8613500000000: 24...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('884', '2017-08-05 16:11:00', '555', '+8613500000000: 25...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('885', '2017-08-05 16:11:00', '556', '+8613500000000: 25...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('886', '2017-08-05 16:11:00', '546', '+8613500000000: 21...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('887', '2017-08-05 16:11:00', '547', '+8613500000000: 21...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('888', '2017-08-05 16:11:00', '550', '+8613500000000: 22...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('889', '2017-08-05 16:11:00', '551', '+8613500000000: 23...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('890', '2017-08-05 16:11:00', '552', '+8613500000000: 23...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('891', '2017-08-05 16:11:00', '548', '+8613500000000: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('892', '2017-08-05 16:11:00', '549', '+8613500000000: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('893', '2017-08-05 16:11:00', '557', 'post: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('894', '2017-08-05 16:11:01', '558', '+8613500000000: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('895', '2017-08-05 16:11:01', '559', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('896', '2017-08-05 16:11:01', '561', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('897', '2017-08-05 16:11:01', '562', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('898', '2017-08-05 16:11:01', '560', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('899', '2017-08-05 16:11:01', '563', '+8613500000000: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('900', '2017-08-05 16:11:01', '564', '+8613500000000: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('901', '2017-08-05 16:11:01', '565', '+8613500000000: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('902', '2017-08-05 16:11:01', '566', '+8613500000000: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('903', '2017-08-05 16:11:01', '567', '+8613500000000: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('904', '2017-08-05 16:11:01', '568', '+8613500000000: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('905', '2017-08-05 16:11:01', '569', '+8613500000000: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('906', '2017-08-05 16:11:01', '570', '+8613500000000: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('907', '2017-08-05 16:11:01', '571', '+8613500000000: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('908', '2017-08-05 16:11:01', '572', '+8613500000000: 10...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('909', '2017-08-05 16:11:01', '573', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('910', '2017-08-05 16:11:01', '574', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('911', '2017-08-05 16:11:01', '575', '+8613500000000: 12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('912', '2017-08-05 16:11:01', '576', '+8613500000000: 12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('913', '2017-08-05 16:11:01', '577', '+8613500000000: 13...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('914', '2017-08-05 16:11:01', '578', '+8613500000000: 13...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('915', '2017-08-05 16:11:01', '579', '+8613500000000: 14...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('916', '2017-08-05 16:11:01', '580', '+8613500000000: 15...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('917', '2017-08-05 16:11:01', '581', '+8613500000000: 15...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('918', '2017-08-05 16:11:01', '582', '+8613500000000: 16...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('919', '2017-08-05 16:11:01', '583', '+8613500000000: 16...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('920', '2017-08-05 16:11:01', '584', '+8613500000000: 17...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('921', '2017-08-05 16:11:01', '585', '+8613500000000: 18...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('922', '2017-08-05 16:11:01', '586', '+8613500000000: 18...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('923', '2017-08-05 16:11:01', '587', '+8613500000000: 19...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('924', '2017-08-05 16:11:02', '588', '+8613500000000: 19...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('925', '2017-08-05 16:11:02', '508', 'post: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('926', '2017-08-05 16:11:02', '509', '+8613500000000: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('927', '2017-08-05 16:11:02', '510', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('928', '2017-08-05 16:11:02', '511', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('929', '2017-08-05 16:11:02', '512', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('930', '2017-08-05 16:11:02', '513', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('931', '2017-08-05 16:11:02', '514', '+8613500000000: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('932', '2017-08-05 16:11:02', '515', '+8613500000000: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('933', '2017-08-05 16:11:02', '516', '+8613500000000: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('934', '2017-08-05 16:11:02', '517', '+8613500000000: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('935', '2017-08-05 16:11:02', '518', '+8613500000000: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('936', '2017-08-05 16:11:02', '519', '+8613500000000: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('937', '2017-08-05 16:11:02', '520', '+8613500000000: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('938', '2017-08-05 16:11:02', '521', '+8613500000000: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('939', '2017-08-05 16:11:02', '522', '+8613500000000: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('940', '2017-08-05 16:11:02', '523', '+8613500000000: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('941', '2017-08-05 16:11:03', '524', '+8613500000000: 10...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('942', '2017-08-05 16:11:03', '525', '+8613500000000: 10...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('943', '2017-08-05 16:11:03', '526', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('944', '2017-08-05 16:11:03', '527', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('945', '2017-08-05 16:11:03', '528', '+8613500000000: 12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('946', '2017-08-05 16:11:03', '529', '+8613500000000: 12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('947', '2017-08-05 16:11:03', '530', '+8613500000000: 13...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('948', '2017-08-05 16:11:03', '531', '+8613500000000: 13...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('949', '2017-08-05 16:11:03', '532', '+8613500000000: 14...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('950', '2017-08-05 16:11:03', '533', '+8613500000000: 14...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('951', '2017-08-05 16:11:03', '534', '+8613500000000: 15...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('952', '2017-08-05 16:11:03', '535', '+8613500000000: 15...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('953', '2017-08-05 16:11:03', '536', '+8613500000000: 16...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('954', '2017-08-05 16:11:03', '537', '+8613500000000: 16...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('955', '2017-08-05 16:11:03', '538', '+8613500000000: 17...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('956', '2017-08-05 16:11:03', '539', '+8613500000000: 17...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('957', '2017-08-05 16:11:03', '540', '+8613500000000: 18...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('958', '2017-08-05 16:11:03', '541', '+8613500000000: 18...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('959', '2017-08-05 16:11:03', '542', '+8613500000000: 19...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('960', '2017-08-05 16:11:03', '543', '+8613500000000: 19...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('961', '2017-08-05 16:11:04', '544', '+8613500000000: 20...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('962', '2017-08-05 16:11:04', '545', '+8613500000000: 20...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('963', '2017-08-05 16:11:04', '553', '+8613500000000: 24...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('964', '2017-08-05 16:11:04', '554', '+8613500000000: 24...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('965', '2017-08-05 16:11:04', '555', '+8613500000000: 25...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('966', '2017-08-05 16:11:04', '556', '+8613500000000: 25...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('967', '2017-08-05 16:11:04', '546', '+8613500000000: 21...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('968', '2017-08-05 16:11:04', '547', '+8613500000000: 21...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('969', '2017-08-05 16:11:04', '550', '+8613500000000: 22...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('970', '2017-08-05 16:11:04', '551', '+8613500000000: 23...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('971', '2017-08-05 16:11:04', '552', '+8613500000000: 23...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('972', '2017-08-05 16:11:04', '548', '+8613500000000: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('973', '2017-08-05 16:11:04', '549', '+8613500000000: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('974', '2017-08-05 16:11:04', '557', 'post: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('975', '2017-08-05 16:11:04', '558', '+8613500000000: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('976', '2017-08-05 16:11:04', '559', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('977', '2017-08-05 16:11:04', '561', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('978', '2017-08-05 16:11:04', '562', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('979', '2017-08-05 16:11:04', '560', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('980', '2017-08-05 16:11:04', '563', '+8613500000000: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('981', '2017-08-05 16:11:04', '564', '+8613500000000: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('982', '2017-08-05 16:11:04', '565', '+8613500000000: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('983', '2017-08-05 16:11:04', '566', '+8613500000000: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('984', '2017-08-05 16:11:04', '567', '+8613500000000: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('985', '2017-08-05 16:11:04', '568', '+8613500000000: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('986', '2017-08-05 16:11:04', '569', '+8613500000000: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('987', '2017-08-05 16:11:04', '570', '+8613500000000: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('988', '2017-08-05 16:11:04', '571', '+8613500000000: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('989', '2017-08-05 16:11:04', '572', '+8613500000000: 10...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('990', '2017-08-05 16:11:04', '573', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('991', '2017-08-05 16:11:04', '574', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('992', '2017-08-05 16:11:04', '575', '+8613500000000: 12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('993', '2017-08-05 16:11:05', '576', '+8613500000000: 12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('994', '2017-08-05 16:11:05', '577', '+8613500000000: 13...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('995', '2017-08-05 16:11:05', '578', '+8613500000000: 13...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('996', '2017-08-05 16:11:05', '579', '+8613500000000: 14...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('997', '2017-08-05 16:11:05', '580', '+8613500000000: 15...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('998', '2017-08-05 16:11:05', '581', '+8613500000000: 15...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('999', '2017-08-05 16:11:05', '582', '+8613500000000: 16...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1000', '2017-08-05 16:11:05', '583', '+8613500000000: 16...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1001', '2017-08-05 16:11:05', '584', '+8613500000000: 17...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1002', '2017-08-05 16:11:05', '585', '+8613500000000: 18...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1003', '2017-08-05 16:11:05', '586', '+8613500000000: 18...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1004', '2017-08-05 16:11:05', '587', '+8613500000000: 19...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1005', '2017-08-05 16:11:05', '588', '+8613500000000: 19...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1006', '2017-08-05 16:42:00', '589', 'post: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1007', '2017-08-05 16:42:00', '590', '+8613500000000: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1008', '2017-08-05 16:42:00', '591', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1009', '2017-08-05 16:42:00', '592', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1010', '2017-08-05 16:42:00', '593', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1011', '2017-08-05 16:42:00', '594', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1012', '2017-08-05 16:42:00', '595', '+8613500000000: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1013', '2017-08-05 16:42:00', '596', '+8613500000000: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1014', '2017-08-05 16:42:00', '597', '+8613500000000: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1015', '2017-08-05 16:42:00', '598', '+8613500000000: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1016', '2017-08-05 16:42:00', '599', '+8613500000000: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1017', '2017-08-05 16:42:00', '600', '+8613500000000: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1018', '2017-08-05 16:42:00', '601', '+8613500000000: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1019', '2017-08-05 16:42:00', '602', '+8613500000000: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1020', '2017-08-05 16:42:00', '603', '+8613500000000: 10...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1021', '2017-08-05 16:42:00', '604', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1022', '2017-08-05 16:42:00', '605', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1023', '2017-08-05 16:42:00', '606', '+8613500000000: 12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1024', '2017-08-05 16:42:00', '607', '+8613500000000: 13...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1025', '2017-08-05 16:42:00', '608', '+8613500000000: 13...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1026', '2017-08-05 16:42:00', '609', '+8613500000000: 14...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1027', '2017-08-05 16:42:00', '610', '+8613500000000: 14...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1028', '2017-08-05 16:42:00', '611', '+8613500000000: 15...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1029', '2017-08-05 16:42:00', '612', '+8613500000000: 16...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1030', '2017-08-05 16:42:01', '613', '+8613500000000: 16...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1031', '2017-08-05 16:42:01', '614', '+8613500000000: 17...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1032', '2017-08-05 16:42:01', '615', '+8613500000000: 18...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1033', '2017-08-05 16:42:01', '616', '+8613500000000: 18...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1034', '2017-08-05 16:42:01', '617', '+8613500000000: 19...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1035', '2017-08-05 16:42:01', '618', '+8613500000000: 20...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1036', '2017-08-05 16:42:01', '619', '+8613500000000: 20...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1037', '2017-08-05 16:42:01', '620', '+8613500000000: 21...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1038', '2017-08-05 16:42:01', '621', '+8613500000000: 22...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1039', '2017-08-05 16:42:01', '622', '+8613500000000: 22...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1040', '2017-08-05 16:42:01', '623', '+8613500000000: 23...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1041', '2017-08-05 16:42:01', '624', '+8613500000000: 23...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1042', '2017-08-05 16:42:01', '625', '+8613500000000: 24...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1043', '2017-08-05 16:42:01', '626', '+8613500000000: 24...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1044', '2017-08-05 16:42:01', '627', '+8613500000000: 25...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1045', '2017-08-05 16:42:01', '628', '+8613500000000: 25...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1046', '2017-08-05 17:01:04', '629', 'post: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1047', '2017-08-05 17:01:04', '630', '+8613500000000: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1048', '2017-08-05 17:01:04', '631', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1049', '2017-08-05 17:01:04', '632', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1050', '2017-08-05 17:01:04', '633', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1051', '2017-08-05 17:01:04', '634', '+8613500000000: 111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1052', '2017-08-05 17:01:04', '635', '+8613500000000: 111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1053', '2017-08-05 17:01:04', '636', '+8613500000000: 1111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1054', '2017-08-05 17:01:04', '637', '+8613500000000: 1111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1055', '2017-08-05 17:01:04', '638', '+8613500000000: 11111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1056', '2017-08-05 17:01:04', '639', '+8613500000000: 11111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1057', '2017-08-05 17:01:04', '640', '+8613500000000: 111111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1058', '2017-08-05 17:01:04', '641', '+8613500000000: 111111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1059', '2017-08-05 17:01:04', '642', '+8613500000000: 1111111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1060', '2017-08-05 17:01:04', '643', '+8613500000000: 1111111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1061', '2017-08-05 17:01:04', '644', '+8613500000000: 11111111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1062', '2017-08-05 17:01:05', '645', '+8613500000000: 11111111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1063', '2017-08-05 17:01:05', '646', '+8613500000000: 1111111111111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1064', '2017-08-05 17:01:05', '647', '+8613500000000: 1111111111111...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1065', '2017-08-05 17:01:05', '648', '+8613500000000: 1212121...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1066', '2017-08-05 17:01:05', '649', '+8613500000000: 1212121...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1067', '2017-08-05 17:01:05', '650', '+8613500000000: 2222222222222222...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1068', '2017-08-05 17:01:05', '651', '+8613500000000: 2222222222222222...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1069', '2017-08-05 17:01:05', '652', '+8613500000000: 212121222222222222222222222222222222...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1070', '2017-08-05 17:01:05', '653', '+8613500000000: 212121222222222222222222222222222222...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1071', '2017-08-05 17:01:05', '654', '+8613500000000: 3333333333333333333...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1072', '2017-08-05 17:01:05', '655', '+8613500000000: 3333333333333333333...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1073', '2017-08-05 17:01:05', '656', '+8613500000000: 12aaa...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1074', '2017-08-05 17:01:05', '660', '+8613500000000: 1212121212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1075', '2017-08-05 17:01:05', '662', '+8613500000000: 31222222222222222...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1076', '2017-08-05 17:01:05', '663', '+8613500000000: 31222222222222222...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1077', '2017-08-05 17:01:05', '664', '+8613500000000: qewqe...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1078', '2017-08-05 17:01:05', '665', '+8613500000000: qewqe...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1079', '2017-08-05 17:01:05', '666', '+8613500000000: qewqe121212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1080', '2017-08-05 17:01:05', '667', '+8613500000000: qewqe121212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1081', '2017-08-05 17:01:05', '670', '+8613500000000: 121222222222222222...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1082', '2017-08-05 17:01:06', '671', '+8613500000000: 121222222222222222...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1083', '2017-08-05 17:01:06', '661', '+8613500000000: 1212121212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1084', '2017-08-05 17:01:06', '657', '+8613500000000: 12aaa...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1085', '2017-08-05 17:01:06', '672', '+8613500000000: oooooooooooooo...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1086', '2017-08-05 17:01:06', '674', '+8613500000000: oooooooooooooo...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1087', '2017-08-05 17:01:06', '678', '+8613500000000: 1231212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1088', '2017-08-05 17:01:06', '684', '+8613500000000: 121212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1089', '2017-08-05 17:01:06', '685', '+8613500000000: 121212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1090', '2017-08-05 17:01:06', '679', '+8613500000000: 1231212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1091', '2017-08-05 17:01:06', '688', '+8613500000000: xxxx...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1092', '2017-08-05 17:01:06', '689', '+8613500000000: xxxx...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1093', '2017-08-05 17:01:06', '690', '+8613500000000: yyyyy...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1094', '2017-08-05 17:01:06', '691', '+8613500000000: yyyyy...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1095', '2017-08-05 17:01:06', '692', '+8613500000000: zzzzzz...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1096', '2017-08-05 17:01:06', '693', '+8613500000000: zzzzzz...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1097', '2017-08-06 00:04:23', '694', 'post: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1098', '2017-08-06 00:04:23', '695', '+8613500000000: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1099', '2017-08-06 00:04:23', '696', '+8613500000000: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1100', '2017-08-06 00:04:23', '703', '+8613500000000: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1101', '2017-08-06 00:04:23', '704', '+8613500000000: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1102', '2017-08-06 00:04:23', '705', '+8613500000000: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1103', '2017-08-06 00:04:23', '706', '+8613500000000: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1104', '2017-08-06 00:04:23', '729', '+8613500000000: uuuuuuuuuuu...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1105', '2017-08-06 00:04:23', '730', '+8613500000000: uuuuuuuuuuu...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1106', '2017-08-06 00:04:23', '697', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1107', '2017-08-06 00:04:23', '698', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1108', '2017-08-06 00:04:23', '701', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1109', '2017-08-06 00:04:23', '702', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1110', '2017-08-06 00:04:23', '709', '+8613500000000: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1111', '2017-08-06 00:04:23', '710', '+8613500000000: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1112', '2017-08-06 00:04:23', '711', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1113', '2017-08-06 00:04:23', '712', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1114', '2017-08-06 00:04:23', '713', '+8613500000000: 22...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1115', '2017-08-06 00:04:23', '714', '+8613500000000: 22...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1116', '2017-08-06 00:04:23', '719', '+8613500000000: 24...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1117', '2017-08-06 00:04:24', '720', '+8613500000000: 24...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1118', '2017-08-06 00:04:24', '723', '+8613500000000: 25...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1119', '2017-08-06 00:04:24', '724', '+8613500000000: 25...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1120', '2017-08-06 00:04:24', '715', '+8613500000000: 23...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1121', '2017-08-06 00:04:24', '717', '+8613500000000: 23...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1122', '2017-08-06 00:04:24', '725', '+8613500000000: xxx...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1123', '2017-08-06 00:04:24', '726', '+8613500000000: xxx...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1124', '2017-08-06 00:04:24', '727', '+8613500000000: zzzzz...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1125', '2017-08-06 00:04:24', '728', '+8613500000000: zzzzz...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1126', '2017-08-06 00:32:19', '733', 'post: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1127', '2017-08-06 00:32:19', '734', '+8613500000000: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1128', '2017-08-06 00:32:19', '735', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1129', '2017-08-06 00:32:19', '736', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1130', '2017-08-06 00:32:19', '747', '+8613500000000: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1131', '2017-08-06 00:32:19', '749', '+8613500000000: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1132', '2017-08-06 00:32:19', '737', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1133', '2017-08-06 00:32:19', '738', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1134', '2017-08-06 00:32:19', '741', '+8613500000000: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1135', '2017-08-06 00:32:19', '742', '+8613500000000: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1136', '2017-08-06 00:32:19', '743', '+8613500000000: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1137', '2017-08-06 00:32:19', '745', '+8613500000000: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1138', '2017-08-06 00:32:19', '753', '+8613500000000: 121...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1139', '2017-08-06 00:32:19', '754', '+8613500000000: 121...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1140', '2017-08-06 00:32:19', '755', '+8613500000000: zzzzzzzzzzzzzzzzzzz...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1141', '2017-08-06 00:32:19', '756', '+8613500000000: zzzzzzzzzzzzzzzzzzz...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1142', '2017-08-06 00:32:19', '759', '+8613500000000: fsfsd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1143', '2017-08-06 00:32:19', '760', '+8613500000000: fsfsd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1144', '2017-08-06 00:32:19', '761', '+8613500000000: sd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1145', '2017-08-06 00:32:19', '762', '+8613500000000: sd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1146', '2017-08-06 00:32:19', '763', '+8613500000000: ddfdf...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1147', '2017-08-06 00:32:19', '764', '+8613500000000: ddfdf...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1148', '2017-08-06 00:32:19', '765', '+8613500000000: 发的...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1149', '2017-08-06 00:32:19', '766', '+8613500000000: 发的...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1150', '2017-08-06 00:32:20', '767', '+8613500000000: 的...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1151', '2017-08-06 00:32:20', '768', '+8613500000000: 的...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1152', '2017-08-06 00:32:20', '769', '+8613500000000: 发粉色的...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1153', '2017-08-06 00:32:20', '770', '+8613500000000: 发房顶上...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1154', '2017-08-06 00:32:20', '771', '+8613500000000: 发放...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1155', '2017-08-06 00:32:20', '772', '+8613500000000: 啧啧啧...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1156', '2017-08-06 00:32:20', '773', '+8613500000000: 啧啧啧...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1157', '2017-08-06 00:32:20', '774', '+8613500000000: 等答复...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1158', '2017-08-06 00:32:20', '775', '+8613500000000: 费大幅度...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1159', '2017-08-06 00:32:20', '776', '+8613500000000: 反对法东方闪电...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1160', '2017-08-06 00:32:20', '777', '+8613500000000: 放的地方...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1161', '2017-08-06 00:32:20', '778', '+8613500000000: 啊打发...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1162', '2017-08-06 00:38:32', '779', 'post: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1163', '2017-08-06 00:38:32', '780', '+8613500000000: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1164', '2017-08-06 00:38:32', '781', '+8613500000000: 3...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1165', '2017-08-06 00:38:32', '782', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1166', '2017-08-06 00:38:32', '783', '+8613500000000: 4...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1167', '2017-08-06 00:38:32', '784', '+8613500000000: 5...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1168', '2017-08-06 00:38:32', '785', '+8613500000000: 6...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1169', '2017-08-06 00:38:32', '786', '+8613500000000: 7...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1170', '2017-08-06 00:38:32', '787', '+8613500000000: 8...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1171', '2017-08-06 00:38:32', '788', '+8613500000000: 9...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1172', '2017-08-06 00:38:32', '789', '+8613500000000: 10...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1173', '2017-08-06 00:38:32', '790', '+8613500000000: 10...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1174', '2017-08-06 00:38:32', '791', '+8613500000000: 11...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1175', '2017-08-06 00:38:32', '792', '+8613500000000: 12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1176', '2017-08-06 00:38:32', '793', '+8613500000000: 13...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1177', '2017-08-06 00:38:32', '794', '+8613500000000: 14...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1178', '2017-08-06 00:38:32', '795', '+8613500000000: 15...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1179', '2017-08-06 00:38:32', '796', '+8613500000000: 15...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1180', '2017-08-06 01:06:03', '797', '+8613500000000: afdsdafa...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1181', '2017-08-06 01:06:03', '799', '+8613500000000: fafddfafd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1182', '2017-08-06 01:06:03', '800', '+8613500000000: fafddfafd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1183', '2017-08-06 01:06:03', '801', '+8613500000000: fd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1184', '2017-08-06 01:06:03', '802', '+8613500000000: fdafdasfd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1185', '2017-08-06 01:06:03', '803', '+8613500000000: zzzz...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1186', '2017-08-06 01:06:03', '804', '+8613500000000: fadfadfd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1187', '2017-08-06 01:06:03', '805', '+8613500000000: fadfadfd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1188', '2017-08-06 01:06:03', '806', '+8613500000000: zfadf...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1189', '2017-08-06 01:06:03', '807', '+8613500000000: fdadfsdf...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1190', '2017-08-06 01:06:03', '808', '+8613500000000: wewef...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1191', '2017-08-06 01:06:03', '809', '+8613500000000: zzzzzzzzzzzzzz...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1192', '2017-08-06 01:06:03', '810', '+8613500000000: fsdfsdfasdfsdfds...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1193', '2017-08-06 01:06:03', '811', '+8613500000000: fdsafsdf...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1194', '2017-08-06 01:06:03', '812', '+8613500000000: wwwww...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1195', '2017-08-06 01:06:03', '813', '+8613500000000: cccccc...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1196', '2017-08-06 01:06:03', '814', '+8613500000000: ddd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1197', '2017-08-06 01:06:03', '815', '+8613500000000: ddd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1198', '2017-08-06 01:06:03', '816', '+8613500000000: zzz...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1199', '2017-08-06 01:06:03', '817', '+8613500000000: fdfd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1200', '2017-08-06 01:06:03', '818', '+8613500000000: www...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1201', '2017-08-06 01:06:03', '819', '+8613500000000: sss...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1202', '2017-08-06 01:06:03', '820', '+8613500000000: sss...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1203', '2017-08-06 01:06:03', '821', '+8613500000000: dfdfd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1204', '2017-08-06 01:06:03', '822', '+8613500000000: fdfdfd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1205', '2017-08-06 01:06:04', '823', '+8613500000000: fdfdfd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1206', '2017-08-06 01:06:04', '824', '+8613500000000: dsfsd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1207', '2017-08-06 01:12:49', '832', '+8613500000000: 哀悼...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1208', '2017-08-06 01:12:49', '834', '+8613500000000: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1209', '2017-08-06 01:12:49', '835', '+8613500000000: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1210', '2017-08-06 01:12:49', '836', '+8613500000000: 的...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1211', '2017-08-06 01:12:49', '837', '+8613500000000: 的...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1212', '2017-08-06 01:12:49', '833', '+8613500000000: 哀悼...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1213', '2017-08-06 01:12:49', '838', '+8613500000000: 发的胜多负少...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1214', '2017-08-06 01:12:49', '840', '+8613500000000: 发的胜多负少...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1215', '2017-08-06 02:43:36', '844', 'post: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1216', '2017-08-06 02:43:36', '845', '+8613500000000: 大方...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1217', '2017-08-06 02:43:36', '846', '+8613500000000: 发顺丰说...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1218', '2017-08-06 02:43:37', '848', '+8613500000000: 发大水...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1219', '2017-08-06 02:43:37', '849', '+8613500000000: 发大水...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1220', '2017-08-06 02:43:37', '850', '+8613500000000: 发送点...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1221', '2017-08-06 02:43:37', '851', 'post: 123121...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1222', '2017-08-06 02:43:37', '852', 'post: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1223', '2017-08-06 02:43:37', '853', 'post: 1...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1224', '2017-08-06 02:43:37', '855', '+8613500000000: 发辅导费...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1225', '2017-08-06 02:43:37', '856', '+8613500000000: 发大水发...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1226', '2017-08-06 02:43:37', '858', '+8613500000000: 大方...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1227', '2017-08-06 02:43:37', '859', '+8613500000000: 大方...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1228', '2017-08-06 02:43:37', '860', '+8613500000000: 发的...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1229', '2017-08-06 02:43:37', '863', '+8613500000000: 放大...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1230', '2017-08-06 02:43:37', '868', '+8613500000000: 个...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1231', '2017-08-06 02:43:37', '864', '+8613500000000: 放大...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1232', '2017-08-06 02:43:37', '865', '+8613500000000: 达到...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1233', '2017-08-06 02:43:37', '866', '+8613500000000: 达到...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1234', '2017-08-06 02:43:37', '867', '+8613500000000: 发送到发送到...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1235', '2017-08-06 02:43:37', '916', '+8613500000000: dfdafdsfsfasdfasdf...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1236', '2017-08-06 02:43:37', '917', '+8613500000000: dfdafdsfsfasdfasdf...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1237', '2017-08-06 02:43:37', '861', '大: 说端到端端到端...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1238', '2017-08-06 02:43:37', '862', 'post: 大丰收的...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1239', '2017-08-06 02:43:37', '869', '+8613500000000: 放大大方都...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1240', '2017-08-06 02:43:37', '870', '+8613500000000: 放大大方都...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1241', '2017-08-06 02:43:37', '871', '+8613500000000: 大...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1242', '2017-08-06 02:43:37', '873', '+8613500000000: 打发...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1243', '2017-08-06 02:43:37', '874', '+8613500000000: 打发...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1244', '2017-08-06 02:43:37', '875', '打打分: 放大...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1245', '2017-08-06 02:43:37', '876', '的: 地方...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1246', '2017-08-06 02:43:37', '877', '1: 2...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1247', '2017-08-06 02:43:37', '878', 'post: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1248', '2017-08-06 02:43:37', '879', 'post: 12...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1249', '2017-08-06 02:43:37', '880', '+8613500000000: 大声道...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1250', '2017-08-06 02:43:37', '882', 'post: 1212...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1251', '2017-08-06 02:43:37', '883', '地方: fsdfs...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1252', '2017-08-06 02:43:37', '884', '+8613500000000: fda...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1253', '2017-08-06 02:43:37', '885', '+8613500000000: fda...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1254', '2017-08-06 02:43:37', '887', 'post: dsafasd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1255', '2017-08-06 02:43:38', '888', '+8613500000000: fdasd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1256', '2017-08-06 02:43:38', '890', 'post: dasfsd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1257', '2017-08-06 02:43:38', '891', 'post: fd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1258', '2017-08-06 02:43:38', '892', 'post: nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1259', '2017-08-06 02:43:38', '893', 'post: ppppppppppppppppppppp...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1260', '2017-08-06 02:43:38', '894', 'post: 1231...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1261', '2017-08-06 02:43:38', '895', '+8613500000000: 12erwer...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1262', '2017-08-06 02:43:38', '897', 'fdafsd: 123...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1263', '2017-08-06 02:43:38', '898', 'post: 10...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1264', '2017-08-06 02:43:38', '899', 'post: 231...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1265', '2017-08-06 02:43:38', '900', '+8613500000000: dfsagdgd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1266', '2017-08-06 02:43:38', '902', '+8613500000000: dfsagdgd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1267', '2017-08-06 02:43:38', '904', '+8613500000000: dfsagdgd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1268', '2017-08-06 02:43:38', '906', '+8613500000000: dfadfasdffffdfdfd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1269', '2017-08-06 02:43:38', '911', '+8613500000000: fdads...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1270', '2017-08-06 02:43:38', '912', '+8613500000000: fdads...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1271', '2017-08-06 02:43:38', '913', '+8613500000000: fdada...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1272', '2017-08-06 02:43:38', '907', '+8613500000000: dfadfasdffffdfdfd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1273', '2017-08-06 02:43:38', '909', '+8613500000000: dfadfasdffffdfdfd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1274', '2017-08-06 02:43:38', '910', '+8613500000000: dfad...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1275', '2017-08-06 02:43:38', '914', '+8613500000000: fdafsd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1276', '2017-08-06 02:43:39', '915', 'dfafd: dafdfd...', '3', '', '26', '1');
INSERT INTO `django_admin_log` VALUES ('1277', '2017-08-08 15:22:49', '1', 'office ChuangKe', '1', '', '33', '1');
INSERT INTO `django_admin_log` VALUES ('1278', '2017-08-08 15:22:56', '2', 'office Jinqiao', '1', '', '33', '1');
INSERT INTO `django_admin_log` VALUES ('1279', '2017-08-10 14:41:10', '12', 'Office Jinqiao', '3', '', '33', '1');
INSERT INTO `django_admin_log` VALUES ('1280', '2017-08-10 14:41:10', '11', 'Office Jinqiao', '3', '', '33', '1');
INSERT INTO `django_admin_log` VALUES ('1281', '2017-08-10 14:41:10', '10', 'Office Jinqiao', '3', '', '33', '1');
INSERT INTO `django_admin_log` VALUES ('1282', '2017-08-10 14:41:10', '9', 'Office Jinqiao', '3', '', '33', '1');
INSERT INTO `django_admin_log` VALUES ('1283', '2017-08-10 14:41:10', '7', 'Office ChuangKe', '3', '', '33', '1');
INSERT INTO `django_admin_log` VALUES ('1284', '2017-08-10 14:41:10', '6', 'Office ChuangKe', '3', '', '33', '1');
INSERT INTO `django_admin_log` VALUES ('1285', '2017-08-10 14:41:10', '5', 'Office ChuangKe', '3', '', '33', '1');
INSERT INTO `django_admin_log` VALUES ('1286', '2017-08-10 14:41:10', '4', 'Office ChuangKe', '3', '', '33', '1');
INSERT INTO `django_admin_log` VALUES ('1287', '2017-08-10 14:41:10', '3', 'Office ChuangKe', '3', '', '33', '1');
INSERT INTO `django_admin_log` VALUES ('1288', '2017-08-10 14:41:10', '2', 'Office Jinqiao', '3', '', '33', '1');
INSERT INTO `django_admin_log` VALUES ('1289', '2017-08-10 14:41:10', '1', 'Office ChuangKe', '3', '', '33', '1');
INSERT INTO `django_admin_log` VALUES ('1290', '2017-08-20 08:12:02', '8', 'iPhone', '2', '已修改 image 。', '13', '1');
INSERT INTO `django_admin_log` VALUES ('1291', '2017-08-20 12:40:26', '8', 'iPhone', '2', '已修改 image 。', '13', '1');
INSERT INTO `django_admin_log` VALUES ('1292', '2017-08-20 12:49:10', '8', 'iPhone', '2', '已修改 image 。', '13', '1');
INSERT INTO `django_admin_log` VALUES ('1293', '2017-08-21 08:19:04', '25', 'tst', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('1294', '2017-08-21 08:19:04', '27', 'test', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('1295', '2017-08-21 08:19:04', '26', 'test', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('1296', '2017-08-21 08:19:04', '24', 'test', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('1297', '2017-08-21 08:19:04', '23', 'test', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('1298', '2017-08-21 08:19:04', '22', 'test', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('1299', '2017-08-21 08:19:05', '21', 'test', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('1300', '2017-08-21 08:19:05', '20', 'test', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('1301', '2017-08-21 08:19:05', '19', 'test', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('1302', '2017-08-21 08:19:05', '18', 'test', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('1303', '2017-08-21 08:19:05', '17', 'test', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('1304', '2017-08-21 08:19:05', '16', 'test', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('1305', '2017-08-21 08:19:05', '15', 'test', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('1306', '2017-08-21 08:19:05', '14', 'test', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('1307', '2017-08-21 08:19:05', '13', 'test', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('1308', '2017-08-23 14:28:52', '3', 'daily inspection 2', '3', '', '34', '1');
INSERT INTO `django_admin_log` VALUES ('1309', '2017-08-23 14:29:37', '4', 'daily inspection 打发飞凤飞飞凤飞飞凤飞飞凤飞飞凤飞飞凤飞飞飞', '3', '', '34', '1');
INSERT INTO `django_admin_log` VALUES ('1310', '2017-08-23 15:00:28', '8', 'daily inspection 52K14散拍未并拍', '3', '', '34', '1');
INSERT INTO `django_admin_log` VALUES ('1311', '2017-08-23 15:54:04', '6', 'daily inspection 52K14散拍未并拍', '2', '已修改 image_before 。', '34', '1');
INSERT INTO `django_admin_log` VALUES ('1312', '2017-08-23 16:14:03', '7', 'daily inspection 52K14散拍未并拍', '2', '已修改 image_before 。', '34', '1');
INSERT INTO `django_admin_log` VALUES ('1313', '2017-08-23 16:19:31', '7', 'daily inspection 52K14散拍未并拍', '2', '已修改 image_before 。', '34', '1');
INSERT INTO `django_admin_log` VALUES ('1314', '2017-08-23 16:21:03', '7', 'daily inspection 52K14散拍未并拍', '2', '已修改 image_before 。', '34', '1');
INSERT INTO `django_admin_log` VALUES ('1315', '2017-08-23 16:24:16', '7', 'daily inspection 52K14散拍未并拍', '2', '已修改 image_before 。', '34', '1');
INSERT INTO `django_admin_log` VALUES ('1316', '2017-08-23 16:25:16', '7', 'daily inspection 52K14散拍未并拍', '2', '已修改 image_before 。', '34', '1');
INSERT INTO `django_admin_log` VALUES ('1317', '2017-08-23 16:28:43', '7', 'daily inspection 52K14散拍未并拍', '2', '已修改 image_before 。', '34', '1');
INSERT INTO `django_admin_log` VALUES ('1318', '2017-08-23 16:28:54', '7', 'daily inspection 52K14散拍未并拍', '2', '已修改 image_before 。', '34', '1');
INSERT INTO `django_admin_log` VALUES ('1319', '2017-08-23 16:28:54', '7', 'daily inspection 52K14散拍未并拍', '2', '已修改 image_before 。', '34', '1');
INSERT INTO `django_admin_log` VALUES ('1320', '2017-08-23 16:53:51', '7', 'daily inspection 52K14散拍未并拍', '2', '已修改 image_before 。', '34', '1');
INSERT INTO `django_admin_log` VALUES ('1321', '2017-08-24 12:52:40', '1', 'forklift1', '1', '', '35', '1');
INSERT INTO `django_admin_log` VALUES ('1322', '2017-08-24 13:15:36', '1', 'forklift1', '2', '已添加 forklift_image \"forklift_image object\".', '35', '1');
INSERT INTO `django_admin_log` VALUES ('1323', '2017-08-24 13:15:57', '1', 'forklift1', '2', '已添加 forklift_image \"forklift_image object\".', '35', '1');
INSERT INTO `django_admin_log` VALUES ('1324', '2017-08-25 13:02:50', '4', 'automotive', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('1325', '2017-08-25 13:02:52', '5', 'automotive', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('1326', '2017-08-25 13:03:00', '5', 'automotive', '3', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('1327', '2017-08-25 13:03:20', '6', 'chemicals', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('1328', '2017-08-25 13:03:44', '7', 'project and energy', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('1329', '2017-08-25 13:05:48', '3', 'banner3', '2', '已修改 active 。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('1330', '2017-08-25 13:05:53', '2', 'banner2', '2', '已修改 active 。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('1331', '2017-08-25 13:05:57', '1', 'banner1', '2', '已修改 active 。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('1332', '2017-08-25 13:18:38', '3', 'Article object', '2', '已修改 content，abstract 和 image 。', '29', '1');
INSERT INTO `django_admin_log` VALUES ('1333', '2017-08-25 13:19:50', '3', 'Article object', '2', '已修改 title 和 content 。', '29', '1');
INSERT INTO `django_admin_log` VALUES ('1334', '2017-08-25 13:21:08', '2', 'Article object', '2', '已修改 title，content，abstract 和 image 。', '29', '1');
INSERT INTO `django_admin_log` VALUES ('1335', '2017-08-25 13:21:24', '2', 'Article object', '2', '已修改 content 。', '29', '1');
INSERT INTO `django_admin_log` VALUES ('1336', '2017-08-25 13:22:30', '1', 'Article object', '2', '已修改 title，content，abstract 和 image 。', '29', '1');
INSERT INTO `django_admin_log` VALUES ('1337', '2017-08-25 13:22:45', '1', 'Article object', '2', '已修改 content 。', '29', '1');
INSERT INTO `django_admin_log` VALUES ('1338', '2017-08-27 06:08:38', '1', 'shelf object', '1', '', '41', '1');
INSERT INTO `django_admin_log` VALUES ('1339', '2017-08-27 06:13:46', '1', 'shelf_inspection_record object', '1', '', '42', '1');
INSERT INTO `django_admin_log` VALUES ('1340', '2017-08-27 08:17:12', '1', 'shelf_inspection_record object', '2', '没有字段被修改。', '42', '1');
INSERT INTO `django_admin_log` VALUES ('1341', '2017-08-27 08:17:26', '2', 'shelf_inspection_record object', '1', '', '42', '1');
INSERT INTO `django_admin_log` VALUES ('1342', '2017-08-27 08:18:47', '2', 'shelf2 2 2 2 2', '1', '', '41', '1');
INSERT INTO `django_admin_log` VALUES ('1343', '2017-08-27 14:16:29', '1', 'shelf_inspection object', '1', '', '50', '1');
INSERT INTO `django_admin_log` VALUES ('1344', '2017-08-27 14:17:06', '1', 'shelf_inspection object', '2', '已添加 shelf_inspection_record \"shelf_inspection_record object\".', '50', '1');
INSERT INTO `django_admin_log` VALUES ('1345', '2017-08-27 14:17:30', '2', 'shelf_inspection object', '1', '', '50', '1');
INSERT INTO `django_admin_log` VALUES ('1346', '2017-08-27 14:17:45', '2', 'shelf_inspection object', '2', '已添加 shelf_inspection_record \"shelf_inspection_record object\".', '50', '1');

-- ----------------------------
-- Table structure for `django_comments`
-- ----------------------------
DROP TABLE IF EXISTS `django_comments`;
CREATE TABLE `django_comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `object_pk` longtext NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_email` varchar(254) DEFAULT NULL,
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
  KEY `django_comments_user_id_2c584e2_fk_personalcenter_myuser_id` (`user_id`),
  KEY `django_comments_submit_date_5c84a37e_uniq` (`submit_date`),
  CONSTRAINT `django_comments_site_id_6ea83216_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`),
  CONSTRAINT `django_comments_user_id_2c584e2_fk_personalcenter_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `personalcenter_myuser` (`id`),
  CONSTRAINT `django_commen_content_type_id_5626a505_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=952 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_comments
-- ----------------------------
INSERT INTO `django_comments` VALUES ('6', '2', 'csdong', 'navicester@163.com', 'http://zakkabag.applinzi.com/', '6', '2016-12-10 09:51:01', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('7', '2', 'csdong', 'navicester@163.com', 'http://zakkabag.applinzi.com/', '7', '2016-12-10 10:12:33', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('918', '18', 'post', 'bin.he@live.com', '', '1', '2017-08-06 02:43:49', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('919', '18', 'post', 'bin.he@live.com', '', '234', '2017-08-06 02:48:29', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('920', '18', 'post', 'bin.he@live.com', '', '123', '2017-08-06 02:48:47', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('921', '18', '+8613500000000', 'bin.he@live.com', '', 'fdasd', '2017-08-06 02:48:53', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('922', '18', '+8613500000000', 'bin.he@live.com', '', 'fdasd', '2017-08-06 02:48:53', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('925', '18', '+8613500000000', 'bin.he@live.com', '', 'afa', '2017-08-06 02:49:09', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('926', '18', 'post', 'bin.he@live.com', '', 'afdsfsdf', '2017-08-06 02:49:26', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('927', '18', '+8613500000000', 'bin.he@live.com', '', '的', '2017-08-06 02:51:12', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('929', '18', '放大', 'bin.he@live.com', '', '123', '2017-08-06 02:51:27', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('930', '18', 'post', 'navicester@163.com', '', 'dadfdfdafdsfas', '2017-08-06 02:51:45', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('931', '18', 'post', 'navicester@163.com', '', '11111111111111111111111111', '2017-08-06 02:51:59', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('932', '18', '+8613500000000', 'bin.he@live.com', '', 'fd', '2017-08-06 02:53:01', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('933', '18', 'fdasd', 'bin.he@live.com', '', '123', '2017-08-06 02:53:11', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('934', '18', 'fdasd', 'bin.he@live.com', '', '123fdfd', '2017-08-06 02:53:24', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('935', '18', '+8613500000000', 'bin.he@live.com', '', '2', '2017-08-06 02:59:18', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('936', '18', '+8613500000000', 'bin.he@live.com', '', '2', '2017-08-06 02:59:18', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('937', '18', '+8613500000000', 'bin.he@live.com', '', '3', '2017-08-06 02:59:23', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('938', '18', '+8613500000000', 'bin.he@live.com', '', '123', '2017-08-06 02:59:44', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('939', '18', '+8613500000000', 'bin.he@live.com', '', '123', '2017-08-06 02:59:44', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('940', '18', '+8613500000000', 'bin.he@live.com', '', '123123', '2017-08-06 02:59:47', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('941', '18', '+8613500000000', 'bin.he@live.com', '', '123123', '2017-08-06 02:59:47', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('944', '18', '+8613500000000', 'bin.he@live.com', '', '12344', '2017-08-06 02:59:59', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('945', '18', '+8613500000000', 'bin.he@live.com', '', '12344', '2017-08-06 02:59:59', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('946', '18', '+8613500000000', 'bin.he@live.com', '', '1234421212', '2017-08-06 03:00:04', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('947', '18', '+8613500000000', 'bin.he@live.com', '', '1234421212', '2017-08-06 03:00:04', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('950', '18', 'post', 'bin.he@live.com', '', '12131312', '2017-08-06 03:00:32', '127.0.0.1', '1', '0', '25', '1', '1');
INSERT INTO `django_comments` VALUES ('951', '18', 'post', 'bin.he@live.com', '', '1231212', '2017-08-06 03:00:46', '127.0.0.1', '1', '0', '25', '1', '1');

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
  CONSTRAINT `django_comment_flags_user_id_3512f4c_fk_personalcenter_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `personalcenter_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_comment_flags
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
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('30', 'authwrapper', 'myuser');
INSERT INTO `django_content_type` VALUES ('31', 'authwrapper', 'wechatuserprofile');
INSERT INTO `django_content_type` VALUES ('15', 'carts', 'cart');
INSERT INTO `django_content_type` VALUES ('14', 'carts', 'cartitem');
INSERT INTO `django_content_type` VALUES ('26', 'comments', 'mpttcomment');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('25', 'crowdfundings', 'crowdfunding');
INSERT INTO `django_content_type` VALUES ('23', 'django_comments', 'comment');
INSERT INTO `django_content_type` VALUES ('24', 'django_comments', 'commentflag');
INSERT INTO `django_content_type` VALUES ('34', 'inspection', 'dailyinspection');
INSERT INTO `django_content_type` VALUES ('45', 'inspection', 'extinguisher');
INSERT INTO `django_content_type` VALUES ('48', 'inspection', 'extinguisher_inspection');
INSERT INTO `django_content_type` VALUES ('35', 'inspection', 'forklift');
INSERT INTO `django_content_type` VALUES ('39', 'inspection', 'forklift_annual_inspection');
INSERT INTO `django_content_type` VALUES ('40', 'inspection', 'forklift_annual_inspection_image');
INSERT INTO `django_content_type` VALUES ('36', 'inspection', 'forklift_image');
INSERT INTO `django_content_type` VALUES ('37', 'inspection', 'forklift_maint');
INSERT INTO `django_content_type` VALUES ('38', 'inspection', 'forklift_repair');
INSERT INTO `django_content_type` VALUES ('46', 'inspection', 'hydrant');
INSERT INTO `django_content_type` VALUES ('49', 'inspection', 'hydrant_inspection');
INSERT INTO `django_content_type` VALUES ('33', 'inspection', 'officeinspection');
INSERT INTO `django_content_type` VALUES ('47', 'inspection', 'rehearsal');
INSERT INTO `django_content_type` VALUES ('41', 'inspection', 'shelf');
INSERT INTO `django_content_type` VALUES ('43', 'inspection', 'shelf_annual_inspection');
INSERT INTO `django_content_type` VALUES ('44', 'inspection', 'shelf_annual_inspection_image');
INSERT INTO `django_content_type` VALUES ('50', 'inspection', 'shelf_inspection');
INSERT INTO `django_content_type` VALUES ('42', 'inspection', 'shelf_inspection_record');
INSERT INTO `django_content_type` VALUES ('29', 'newsletter', 'article');
INSERT INTO `django_content_type` VALUES ('28', 'newsletter', 'banner');
INSERT INTO `django_content_type` VALUES ('7', 'newsletter', 'signup');
INSERT INTO `django_content_type` VALUES ('18', 'orders', 'order');
INSERT INTO `django_content_type` VALUES ('17', 'orders', 'useraddress');
INSERT INTO `django_content_type` VALUES ('16', 'orders', 'usercheckout');
INSERT INTO `django_content_type` VALUES ('27', 'personalcenter', 'userprofile');
INSERT INTO `django_content_type` VALUES ('32', 'phone_login', 'phonetoken');
INSERT INTO `django_content_type` VALUES ('12', 'products', 'category');
INSERT INTO `django_content_type` VALUES ('9', 'products', 'product');
INSERT INTO `django_content_type` VALUES ('13', 'products', 'productfeatured');
INSERT INTO `django_content_type` VALUES ('11', 'products', 'productimage');
INSERT INTO `django_content_type` VALUES ('10', 'products', 'variation');
INSERT INTO `django_content_type` VALUES ('21', 'registration', 'registrationprofile');
INSERT INTO `django_content_type` VALUES ('5', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('6', 'sites', 'site');
INSERT INTO `django_content_type` VALUES ('22', 'threadedcomments', 'threadedcomment');

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
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2016-11-27 16:01:58');
INSERT INTO `django_migrations` VALUES ('2', 'contenttypes', '0002_remove_content_type_name', '2016-11-27 16:01:59');
INSERT INTO `django_migrations` VALUES ('3', 'auth', '0001_initial', '2016-11-27 16:02:00');
INSERT INTO `django_migrations` VALUES ('4', 'auth', '0002_alter_permission_name_max_length', '2016-11-27 16:02:00');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0003_alter_user_email_max_length', '2016-11-27 16:02:00');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0004_alter_user_username_opts', '2016-11-27 16:02:00');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0005_alter_user_last_login_null', '2016-11-27 16:02:00');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0006_require_contenttypes_0002', '2016-11-27 16:02:00');
INSERT INTO `django_migrations` VALUES ('9', 'personalcenter', '0001_initial', '2016-11-27 16:02:02');
INSERT INTO `django_migrations` VALUES ('10', 'admin', '0001_initial', '2016-11-27 16:02:02');
INSERT INTO `django_migrations` VALUES ('11', 'products', '0001_initial', '2016-11-27 16:02:03');
INSERT INTO `django_migrations` VALUES ('12', 'products', '0002_variation', '2016-11-27 16:02:03');
INSERT INTO `django_migrations` VALUES ('13', 'products', '0003_productimage', '2016-11-27 16:02:03');
INSERT INTO `django_migrations` VALUES ('14', 'products', '0004_auto_20160927_0832', '2016-11-27 16:02:04');
INSERT INTO `django_migrations` VALUES ('15', 'products', '0005_auto_20161002_1626', '2016-11-27 16:02:05');
INSERT INTO `django_migrations` VALUES ('16', 'products', '0006_productfeatured', '2016-11-27 16:02:05');
INSERT INTO `django_migrations` VALUES ('17', 'carts', '0001_initial', '2016-11-27 16:02:07');
INSERT INTO `django_migrations` VALUES ('18', 'carts', '0002_cartitem_line_item_total', '2016-11-27 16:02:08');
INSERT INTO `django_migrations` VALUES ('19', 'carts', '0003_cart_subtotal', '2016-11-27 16:02:08');
INSERT INTO `django_migrations` VALUES ('20', 'carts', '0004_auto_20161007_1052', '2016-11-27 16:02:09');
INSERT INTO `django_migrations` VALUES ('21', 'carts', '0005_cart_tax_percentage', '2016-11-27 16:02:09');
INSERT INTO `django_migrations` VALUES ('22', 'newsletter', '0001_initial', '2016-11-27 16:02:09');
INSERT INTO `django_migrations` VALUES ('23', 'newsletter', '0002_userwechat', '2016-11-27 16:02:09');
INSERT INTO `django_migrations` VALUES ('24', 'orders', '0001_initial', '2016-11-27 16:02:10');
INSERT INTO `django_migrations` VALUES ('25', 'orders', '0002_useraddress', '2016-11-27 16:02:10');
INSERT INTO `django_migrations` VALUES ('26', 'orders', '0003_order', '2016-11-27 16:02:12');
INSERT INTO `django_migrations` VALUES ('27', 'orders', '0004_order_status', '2016-11-27 16:02:12');
INSERT INTO `django_migrations` VALUES ('28', 'orders', '0005_auto_20161022_1051', '2016-11-27 16:02:12');
INSERT INTO `django_migrations` VALUES ('29', 'personalcenter', '0002_auto_20161127_1857', '2016-11-27 16:02:12');
INSERT INTO `django_migrations` VALUES ('30', 'personalcenter', '0003_auto_20161127_2140', '2016-11-27 16:02:17');
INSERT INTO `django_migrations` VALUES ('31', 'personalcenter', '0004_remove_myuser_identifier', '2016-11-27 16:02:18');
INSERT INTO `django_migrations` VALUES ('32', 'registration', '0001_initial', '2016-11-27 16:02:19');
INSERT INTO `django_migrations` VALUES ('33', 'registration', '0002_registrationprofile_activated', '2016-11-27 16:02:19');
INSERT INTO `django_migrations` VALUES ('34', 'registration', '0003_migrate_activatedstatus', '2016-11-27 16:02:19');
INSERT INTO `django_migrations` VALUES ('35', 'sessions', '0001_initial', '2016-11-27 16:02:19');
INSERT INTO `django_migrations` VALUES ('36', 'sites', '0001_initial', '2016-11-27 16:02:20');
INSERT INTO `django_migrations` VALUES ('37', 'personalcenter', '0005_auto_20161202_1159', '2016-12-02 03:59:54');
INSERT INTO `django_migrations` VALUES ('38', 'personalcenter', '0006_auto_20161202_2124', '2016-12-02 13:24:27');
INSERT INTO `django_migrations` VALUES ('39', 'personalcenter', '0007_myuser_image', '2016-12-03 03:11:15');
INSERT INTO `django_migrations` VALUES ('40', 'django_comments', '0001_initial', '2016-12-04 03:00:07');
INSERT INTO `django_migrations` VALUES ('41', 'django_comments', '0002_update_user_email_field_length', '2016-12-04 03:00:08');
INSERT INTO `django_migrations` VALUES ('42', 'django_comments', '0003_add_submit_date_index', '2016-12-04 03:00:08');
INSERT INTO `django_migrations` VALUES ('43', 'threadedcomments', '0001_initial', '2016-12-04 03:00:09');
INSERT INTO `django_migrations` VALUES ('44', 'threadedcomments', '0002_auto_20150521_2011', '2016-12-04 03:00:09');
INSERT INTO `django_migrations` VALUES ('45', 'crowdfundings', '0001_initial', '2016-12-04 14:19:57');
INSERT INTO `django_migrations` VALUES ('46', 'comments', '0001_initial', '2016-12-10 09:28:57');
INSERT INTO `django_migrations` VALUES ('47', 'crowdfundings', '0002_auto_20161224_1500', '2016-12-24 07:03:21');
INSERT INTO `django_migrations` VALUES ('48', 'personalcenter', '0008_userprofile', '2017-03-26 07:37:46');
INSERT INTO `django_migrations` VALUES ('49', 'personalcenter', '0009_auto_20170326_1536', '2017-03-26 07:37:46');
INSERT INTO `django_migrations` VALUES ('50', 'orders', '0006_auto_20170326_2210', '2017-03-26 14:11:03');
INSERT INTO `django_migrations` VALUES ('51', 'personalcenter', '0010_auto_20170406_2332', '2017-04-06 15:34:03');
INSERT INTO `django_migrations` VALUES ('52', 'newsletter', '0003_banner', '2017-04-29 01:13:35');
INSERT INTO `django_migrations` VALUES ('53', 'newsletter', '0004_article', '2017-04-30 04:38:46');
INSERT INTO `django_migrations` VALUES ('54', 'newsletter', '0005_auto_20170624_1138', '2017-06-24 03:39:13');
INSERT INTO `django_migrations` VALUES ('55', 'personalcenter', '0011_auto_20170624_1138', '2017-06-24 03:39:13');
INSERT INTO `django_migrations` VALUES ('56', 'personalcenter', '0012_auto_20170624_1913', '2017-06-24 11:14:03');
INSERT INTO `django_migrations` VALUES ('57', 'personalcenter', '0013_auto_20170625_0926', '2017-06-25 01:34:57');
INSERT INTO `django_migrations` VALUES ('58', 'personalcenter', '0014_auto_20170625_1552', '2017-06-25 07:52:31');
INSERT INTO `django_migrations` VALUES ('59', 'personalcenter', '0015_auto_20170709_1144', '2017-07-09 11:08:32');
INSERT INTO `django_migrations` VALUES ('60', 'personalcenter', '0016_auto_20170709_1957', '2017-07-09 11:57:52');
INSERT INTO `django_migrations` VALUES ('61', 'personalcenter', '0017_auto_20170709_2014', '2017-07-09 12:14:42');
INSERT INTO `django_migrations` VALUES ('62', 'authwrapper', '0001_initial', '2017-07-09 13:12:02');
INSERT INTO `django_migrations` VALUES ('63', 'authwrapper', '0002_wechatuserprofile', '2017-07-09 13:12:03');
INSERT INTO `django_migrations` VALUES ('64', 'authwrapper', '0003_auto_20170710_0758', '2017-07-09 23:58:27');
INSERT INTO `django_migrations` VALUES ('65', 'newsletter', '0006_delete_userwechat', '2017-07-15 04:27:44');
INSERT INTO `django_migrations` VALUES ('66', 'inspection', '0001_initial', '2017-08-08 15:22:10');
INSERT INTO `django_migrations` VALUES ('67', 'inspection', '0002_officeinspection_comments', '2017-08-10 14:56:34');
INSERT INTO `django_migrations` VALUES ('68', 'inspection', '0003_officeinspection_power', '2017-08-10 14:58:01');
INSERT INTO `django_migrations` VALUES ('69', 'inspection', '0004_auto_20170810_2341', '2017-08-10 15:41:31');
INSERT INTO `django_migrations` VALUES ('70', 'inspection', '0005_officeinspection_image', '2017-08-11 15:46:31');
INSERT INTO `django_migrations` VALUES ('71', 'inspection', '0006_dailyinspection', '2017-08-14 15:08:21');
INSERT INTO `django_migrations` VALUES ('72', 'inspection', '0007_dailyinspection_due_date', '2017-08-14 15:32:12');
INSERT INTO `django_migrations` VALUES ('73', 'inspection', '0008_auto_20170824_2041', '2017-08-24 12:41:50');
INSERT INTO `django_migrations` VALUES ('74', 'inspection', '0009_auto_20170826_1415', '2017-08-26 06:16:57');
INSERT INTO `django_migrations` VALUES ('75', 'inspection', '0010_auto_20170826_1438', '2017-08-26 06:38:49');
INSERT INTO `django_migrations` VALUES ('76', 'inspection', '0011_auto_20170826_1528', '2017-08-26 07:29:02');
INSERT INTO `django_migrations` VALUES ('77', 'inspection', '0012_extinguisher_inspection_hydrant_inspection', '2017-08-26 07:40:56');
INSERT INTO `django_migrations` VALUES ('78', 'inspection', '0013_auto_20170827_2203', '2017-08-28 00:32:19');
INSERT INTO `django_migrations` VALUES ('79', 'inspection', '0014_delete_shelf_inspection', '2017-08-28 00:32:19');
INSERT INTO `django_migrations` VALUES ('80', 'inspection', '0015_auto_20170828_0819', '2017-08-28 00:35:14');

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
INSERT INTO `django_session` VALUES ('0qtzqi61uhdphrvpk1jzculwcd3xzil8', 'Mzc3MWQyOWZhZGJhYzU0MWVhZTQwYjU1M2E2NzZkMjc4MWM3YzA5Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwid2VjaGF0X2lkIjoyMSwiX2F1dGhfdXNlcl9oYXNoIjoiNjYwNDFhM2ZkMmU4MmZmNmNkYmVhMmQ5YTE1ZDJjMTQyZmFlYWE3NyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6InBlcnNvbmFsY2VudGVyLmJhY2tlbmRzLmF1dGguTXlCYWNrZW5kIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-01-09 14:34:54');
INSERT INTO `django_session` VALUES ('1a41ayt9htwk48j9t3t8zukm2u5q7mbp', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-07-29 01:59:58');
INSERT INTO `django_session` VALUES ('1h7e8uao8sz6465rvh9uk4pr0v1ia93p', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-08-22 14:12:30');
INSERT INTO `django_session` VALUES ('29mnkcvyqzp7sqcrjha5g1w1ud4jchjm', 'YmU0NTM4NjFlNmYxYTE3OTVjNDk2MDAzYWQzNDIzODUwYzA0NzhjYzp7IndlY2hhdF9pZCI6MzIsImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-06-04 16:21:48');
INSERT INTO `django_session` VALUES ('3pourynmka94k2icdkcy93ukhlez4j59', 'MDg5OTk3YWMxMGIyYWU5NjM0YjQ3NjMyY2E3YjdhOTUxNzhmZGQ4ZDp7IndlY2hhdF9pZCI6MzAsImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-06-04 16:15:48');
INSERT INTO `django_session` VALUES ('3xq63hhppt7ijonz8f8nb6sdw1dc26yp', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-08-20 01:12:09');
INSERT INTO `django_session` VALUES ('3yuyh517hionuh78nzpo6x2l4t0w5n8l', 'ODAxNWM3Mjk4ZjNhYjJkN2I1NTEwNDE4ZjY4ODk3NjAzZmQwNzBmOTp7IndlY2hhdF9pZCI6MiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-07-29 03:39:28');
INSERT INTO `django_session` VALUES ('415qa89cd31gjj77h570fcwqdfui1hpg', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-07-29 06:28:49');
INSERT INTO `django_session` VALUES ('4w86p2g2esfmr42vekkf1pqji9nk3ecd', 'OGIxYzFmYjY3NjBmMzRmNzNiOGQ3MDczMmI5NDc4NzUwNWVlYzMyZDp7IndlY2hhdF9pZCI6MjcsImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-06-04 16:05:23');
INSERT INTO `django_session` VALUES ('5b656ldw8ma6ui2ntc4uy2h3qobrqnk7', 'OTM1ZDRkMzQ3ZmM5MzI5ZjI0YjgxZjg0ODU2ZWY0ZTNlMDdjZWM3NDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoicGVyc29uYWxjZW50ZXIuYmFja2VuZHMuYXV0aC5NeUJhY2tlbmQiLCJfc2Vzc2lvbl9leHBpcnkiOjAsImNhcnRfaXRlbV9jb3VudCI6MSwidXNlcl9jaGVja291dF9pZCI6MSwiX2F1dGhfdXNlcl9oYXNoIjoiNjYwNDFhM2ZkMmU4MmZmNmNkYmVhMmQ5YTE1ZDJjMTQyZmFlYWE3NyIsImNhcnRfaWQiOjEwfQ==', '2017-04-20 16:12:37');
INSERT INTO `django_session` VALUES ('60fe4tbgx40crawaam1uquqe1m6zqb7a', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-01-08 15:00:54');
INSERT INTO `django_session` VALUES ('69l041mfn2p4992jq23hmh0545riyuf0', 'M2ZjY2I3NjQ5ZmY4OWJjNzE1ZDQxNDVjMzNmN2Y1YzZhN2NiMzQ1ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjY2MDQxYTNmZDJlODJmZjZjZGJlYTJkOWExNWQyYzE0MmZhZWFhNzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJwZXJzb25hbGNlbnRlci5iYWNrZW5kcy5hdXRoLk15QmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-01-07 08:54:30');
INSERT INTO `django_session` VALUES ('6gzgzu5cgd6im03jye8cqhb8e200q9aq', 'NmViZmE2OWQ3ZTEzYTRlN2RjNWRkOTVkZjA3NGQ5NjBlMWE1MGQ2Yzp7Il9hdXRoX3VzZXJfaGFzaCI6ImY4Njg0ZTE0OGExZDk1ODQ2OWE2NDVjZDNmYzNlMjQxNTQwZTM4YzEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJwZXJzb25hbGNlbnRlci5iYWNrZW5kcy5hdXRoLldlY2hhdEJhY2tlbmQiLCJfYXV0aF91c2VyX2lkIjoiNCIsImNhcnRfaXRlbV9jb3VudCI6MH0=', '2016-12-14 07:41:56');
INSERT INTO `django_session` VALUES ('6mg4r9ok48o06t02pjpnczy88tlopxi9', 'NjY2ZDNlYTljNzBhNjQ4ZWUwYTFlYmEzOWRiNDAzMzFjOGM3MmJhZjp7IndlY2hhdF9pZCI6MjUsImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-06-04 15:56:24');
INSERT INTO `django_session` VALUES ('6mi9wmzp5lmegb63hbuq1udoqwwb0fx2', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-07-29 02:15:54');
INSERT INTO `django_session` VALUES ('74iqx2x7nde094awku3nw1zep83wt5y8', 'M2ZjY2I3NjQ5ZmY4OWJjNzE1ZDQxNDVjMzNmN2Y1YzZhN2NiMzQ1ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjY2MDQxYTNmZDJlODJmZjZjZGJlYTJkOWExNWQyYzE0MmZhZWFhNzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJwZXJzb25hbGNlbnRlci5iYWNrZW5kcy5hdXRoLk15QmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2016-12-31 13:36:16');
INSERT INTO `django_session` VALUES ('77fy47ug9r3lzuvmij3aeunu10ubl30o', 'NDMwNTJhNTAxMzJiNWQzNDc1YWQwOTIwNDU0YmI2N2RlOWI5YjVlNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjVmNzY3NjE0NDg3NWUzNjU1ZGU5MmRjNmRhODY2NTUyM2I2YmRjYzEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhdXRod3JhcHBlci5iYWNrZW5kcy5hdXRoLk15QmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-09-03 12:40:12');
INSERT INTO `django_session` VALUES ('7sly3v017gh6npyk1cqhoz6pd2txvbua', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2016-12-16 11:49:30');
INSERT INTO `django_session` VALUES ('7yv2t5z6za5ihg9haxhvwa8qh8lpd6aa', 'Mzc3MWQyOWZhZGJhYzU0MWVhZTQwYjU1M2E2NzZkMjc4MWM3YzA5Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwid2VjaGF0X2lkIjoyMSwiX2F1dGhfdXNlcl9oYXNoIjoiNjYwNDFhM2ZkMmU4MmZmNmNkYmVhMmQ5YTE1ZDJjMTQyZmFlYWE3NyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6InBlcnNvbmFsY2VudGVyLmJhY2tlbmRzLmF1dGguTXlCYWNrZW5kIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-05-20 11:46:07');
INSERT INTO `django_session` VALUES ('7zm7bdrzzseywubp75a8sqs7mvekv9es', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-07-08 15:46:30');
INSERT INTO `django_session` VALUES ('8gx5jjrnhbuedg2c6ofgv10686idn1oy', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-07-08 15:21:27');
INSERT INTO `django_session` VALUES ('8jwiv2cfgs4rsyothqdoxetfwn6g0ygu', 'NzNhZGZiMWY3M2M5ZDE0M2M2N2Y0ZWYzNTMxNTQ0ZTA3OTUzMDUyMTp7IndlY2hhdF9pZCI6MzQsImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-06-04 16:35:50');
INSERT INTO `django_session` VALUES ('9fu4dr7272xwbzs1ulqnlb38y6v5hnlr', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-07-08 15:34:10');
INSERT INTO `django_session` VALUES ('9y31c6pk03ctxl3stwcfv9d26r45217b', 'MjExMWY1ZGFiN2JlYjFjZjNjYmVhMTM5YzM5MzVkMzcwMjU2YzIzNjp7IndlY2hhdF9pZCI6MjQsImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-06-04 15:55:37');
INSERT INTO `django_session` VALUES ('9zptox75d2fohnyts27q87wzfw5fca9l', 'YzU5NjFhN2IyMWY4MWFlNWY1ZmE4ZWU4NGY0NTIyMTlmYzBmNzQxODp7IndlY2hhdF9pZCI6MjksImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-06-04 16:12:30');
INSERT INTO `django_session` VALUES ('b3ivcrjx8p4ruy3bzs3p9dtq8gweva1i', 'OGUzNzM2YjUwOTEzZGY3MzBkYWM2OGI3NmVmMjU2ZTYwMTVlZmY3Zjp7IndlY2hhdF9pZCI6NCwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-08-26 06:44:54');
INSERT INTO `django_session` VALUES ('b4mt2xzsns7ryk4may0zc1kkrd1s2g4y', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-07-27 15:57:36');
INSERT INTO `django_session` VALUES ('bchek8qhq0xkj898pzsgoyc0cf397l2y', 'YmYyMTQ0MTcwZjIyZGI0NDliNTMwYmY4MTExN2M4NjRiYTc4NjEzNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjVmNzY3NjE0NDg3NWUzNjU1ZGU5MmRjNmRhODY2NTUyM2I2YmRjYzEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhdXRod3JhcHBlci5iYWNrZW5kcy5hdXRoLk15QmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2017-08-20 14:00:17');
INSERT INTO `django_session` VALUES ('bss7f6c7gec859z7ue7cieom4r1547on', 'M2ZjY2I3NjQ5ZmY4OWJjNzE1ZDQxNDVjMzNmN2Y1YzZhN2NiMzQ1ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjY2MDQxYTNmZDJlODJmZjZjZGJlYTJkOWExNWQyYzE0MmZhZWFhNzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJwZXJzb25hbGNlbnRlci5iYWNrZW5kcy5hdXRoLk15QmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2016-12-31 08:17:40');
INSERT INTO `django_session` VALUES ('c4lc0btu7t7mfvpinwkxn8qmt83ni3vv', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-05-14 09:09:16');
INSERT INTO `django_session` VALUES ('cjsskjh28vqa7pmmjz62ylo9pouyvwty', 'ZWY0ZjQ0MWM5MzEyN2M0ZmMxMjFmNWFjMWU4MDFkYjc3ZGNlM2Y4Nzp7IndlY2hhdF9pZCI6MjMsImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-06-04 15:54:43');
INSERT INTO `django_session` VALUES ('cnepbvr4hf4kgz7hoyi9e02f5xg8gpjp', 'OGUzNzM2YjUwOTEzZGY3MzBkYWM2OGI3NmVmMjU2ZTYwMTVlZmY3Zjp7IndlY2hhdF9pZCI6NCwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2016-12-14 05:48:39');
INSERT INTO `django_session` VALUES ('d2h11u8qz41zj48w8c8d7vln91zv825l', 'YThmZjZhYjdmYWFlNDMzN2M2ZjkyNGRlNmQ5MWExYTJjMDVhZDljNDp7IndlY2hhdF9pZCI6MjYsImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-06-04 16:00:36');
INSERT INTO `django_session` VALUES ('dzmgdu2no1g4qp37q49xyk3z5927w14d', 'M2ZjY2I3NjQ5ZmY4OWJjNzE1ZDQxNDVjMzNmN2Y1YzZhN2NiMzQ1ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjY2MDQxYTNmZDJlODJmZjZjZGJlYTJkOWExNWQyYzE0MmZhZWFhNzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJwZXJzb25hbGNlbnRlci5iYWNrZW5kcy5hdXRoLk15QmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-01-09 14:51:10');
INSERT INTO `django_session` VALUES ('e14ag4k0bjy54xe28lefgt7kl4hm7b4u', 'NzQ2ZjhlMDZlNTBlODFmY2YzYjljNzBlZWEwNDczODEzZWYyMTcwYTp7Il9hdXRoX3VzZXJfaGFzaCI6IjVmNzY3NjE0NDg3NWUzNjU1ZGU5MmRjNmRhODY2NTUyM2I2YmRjYzEiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImF1dGh3cmFwcGVyLmJhY2tlbmRzLmF1dGguTXlCYWNrZW5kIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-08-27 23:59:13');
INSERT INTO `django_session` VALUES ('ejzd0mtkdzig9qc5w2thiwrrg07wqmfz', 'YjExZDg3N2E4YTZhMWVjYWQ0ZTRjOGJkNDg4N2U1OGRiMDlmMjE3MTp7Il9hdXRoX3VzZXJfaGFzaCI6IjhlZjZmMjBmNGMxNDZmZjgzYTM3YTM4NzQ5NTBkMDUwZTNhZGNlMjUiLCJfYXV0aF91c2VyX2lkIjoiMTEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJwZXJzb25hbGNlbnRlci5iYWNrZW5kcy5hdXRoLldlY2hhdEJhY2tlbmQiLCJSRUdJU1RSQVRJT05fQVVUT19MT0dJTiI6dHJ1ZSwiY2FydF9pdGVtX2NvdW50IjowLCJ3ZWNoYXRfaWQiOjIwfQ==', '2016-12-16 16:14:39');
INSERT INTO `django_session` VALUES ('ey2wbjvktrq128crtj2wgrdnplmulq5m', 'MDRlOTQxNTg4YTBmYmU2OGUwYmQzYTUxOTNkYzgwZDA0ZjNlNjcwNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY2MDQxYTNmZDJlODJmZjZjZGJlYTJkOWExNWQyYzE0MmZhZWFhNzciLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6InBlcnNvbmFsY2VudGVyLmJhY2tlbmRzLmF1dGguTXlCYWNrZW5kIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-02-21 15:11:49');
INSERT INTO `django_session` VALUES ('g5xdownfaf506a9zjp3cia0vm11kd2ju', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-03-17 15:41:41');
INSERT INTO `django_session` VALUES ('gbwa58p52r68xnybzycr2npcsivsg92w', 'M2ZjY2I3NjQ5ZmY4OWJjNzE1ZDQxNDVjMzNmN2Y1YzZhN2NiMzQ1ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjY2MDQxYTNmZDJlODJmZjZjZGJlYTJkOWExNWQyYzE0MmZhZWFhNzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJwZXJzb25hbGNlbnRlci5iYWNrZW5kcy5hdXRoLk15QmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2016-12-31 12:05:17');
INSERT INTO `django_session` VALUES ('gkb9rwjolw3h0lmkt9pklixe4cffjica', 'NTVmNWZmYzVlYmE1YmI2ZDI2YzBjZDRjZTI4YjA5ZGIzMDdhNDZiNDp7IndlY2hhdF9pZCI6MSwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-07-23 13:38:03');
INSERT INTO `django_session` VALUES ('h77x8zfm3h51onzxf7y370l74b4wv0fj', 'M2ZjY2I3NjQ5ZmY4OWJjNzE1ZDQxNDVjMzNmN2Y1YzZhN2NiMzQ1ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjY2MDQxYTNmZDJlODJmZjZjZGJlYTJkOWExNWQyYzE0MmZhZWFhNzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJwZXJzb25hbGNlbnRlci5iYWNrZW5kcy5hdXRoLk15QmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2016-12-31 10:23:04');
INSERT INTO `django_session` VALUES ('hyi23kapytn06w40055t3tjkd25etsor', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-07-29 02:25:28');
INSERT INTO `django_session` VALUES ('ilg97cww08d3w1c2d71yszlekzhzc2ex', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-07-08 15:35:11');
INSERT INTO `django_session` VALUES ('ivv0dqhwjd9jc8d5hqz7faabws1a52n7', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2016-12-12 13:32:47');
INSERT INTO `django_session` VALUES ('ja05rsf206nxtw5vnyi4rkeih3iv7xgq', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-07-29 12:53:28');
INSERT INTO `django_session` VALUES ('kczcidt20n0zy4gjsdvubm8ldkeveuvb', 'MDRlOTQxNTg4YTBmYmU2OGUwYmQzYTUxOTNkYzgwZDA0ZjNlNjcwNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY2MDQxYTNmZDJlODJmZjZjZGJlYTJkOWExNWQyYzE0MmZhZWFhNzciLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6InBlcnNvbmFsY2VudGVyLmJhY2tlbmRzLmF1dGguTXlCYWNrZW5kIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2016-12-31 06:36:30');
INSERT INTO `django_session` VALUES ('kf1c0h4cv3bbb8jimvoaxnb89g6e7iqn', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-07-29 01:58:49');
INSERT INTO `django_session` VALUES ('kuv46n3hqt2uv6jy13lke66kh60v4bey', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-03-17 14:14:05');
INSERT INTO `django_session` VALUES ('l389j5yea8esjlo339tz7ueghyc1yemr', 'NjBjMDQwODZlYmQ4ZTUyZTE5M2JmNzg1M2Q0MjZhYjE4ZTVlOTRhZjp7IndlY2hhdF9pZCI6MjAsIl9hdXRoX3VzZXJfaGFzaCI6IjhlZjZmMjBmNGMxNDZmZjgzYTM3YTM4NzQ5NTBkMDUwZTNhZGNlMjUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJwZXJzb25hbGNlbnRlci5iYWNrZW5kcy5hdXRoLldlY2hhdEJhY2tlbmQiLCJfYXV0aF91c2VyX2lkIjoiMTEiLCJjYXJ0X2l0ZW1fY291bnQiOjB9', '2017-04-02 08:32:52');
INSERT INTO `django_session` VALUES ('lbzpcck9ainwa1ydlucyjetfn5fvnyyi', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-08-20 10:39:01');
INSERT INTO `django_session` VALUES ('lo5uzrosscca075zvez7lylv7r1rx2re', 'ODU1YjVlZTFhYzJkYTU5YTJkZTA3OTJhYzBjOTY1ZWIwYWJmZGMzZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwid2VjaGF0X2lkIjoyMCwiX2F1dGhfdXNlcl9oYXNoIjoiNjYwNDFhM2ZkMmU4MmZmNmNkYmVhMmQ5YTE1ZDJjMTQyZmFlYWE3NyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6InBlcnNvbmFsY2VudGVyLmJhY2tlbmRzLmF1dGguV2VjaGF0QmFja2VuZCIsImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-06-04 14:57:20');
INSERT INTO `django_session` VALUES ('lvyxzkgojqjjxz9ctoe1m2mjyvy4nnsb', 'MDRlOTQxNTg4YTBmYmU2OGUwYmQzYTUxOTNkYzgwZDA0ZjNlNjcwNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY2MDQxYTNmZDJlODJmZjZjZGJlYTJkOWExNWQyYzE0MmZhZWFhNzciLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6InBlcnNvbmFsY2VudGVyLmJhY2tlbmRzLmF1dGguTXlCYWNrZW5kIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2016-12-18 03:22:30');
INSERT INTO `django_session` VALUES ('md3ahs1mjvpjr88ssul97v4vcuoajqzy', 'M2ZjY2I3NjQ5ZmY4OWJjNzE1ZDQxNDVjMzNmN2Y1YzZhN2NiMzQ1ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjY2MDQxYTNmZDJlODJmZjZjZGJlYTJkOWExNWQyYzE0MmZhZWFhNzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJwZXJzb25hbGNlbnRlci5iYWNrZW5kcy5hdXRoLk15QmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2016-12-31 09:11:34');
INSERT INTO `django_session` VALUES ('mifv9gxja732i7oplnapv5wyn6zoy360', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-07-08 15:33:10');
INSERT INTO `django_session` VALUES ('mjtghbxyyrpralh5ugoc2pom4plx93bn', 'NDMwNTJhNTAxMzJiNWQzNDc1YWQwOTIwNDU0YmI2N2RlOWI5YjVlNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjVmNzY3NjE0NDg3NWUzNjU1ZGU5MmRjNmRhODY2NTUyM2I2YmRjYzEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhdXRod3JhcHBlci5iYWNrZW5kcy5hdXRoLk15QmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-08-20 03:00:23');
INSERT INTO `django_session` VALUES ('mtrkwz1paosafwvygdx8wtmafa9vbxsr', 'NzQ2ZjhlMDZlNTBlODFmY2YzYjljNzBlZWEwNDczODEzZWYyMTcwYTp7Il9hdXRoX3VzZXJfaGFzaCI6IjVmNzY3NjE0NDg3NWUzNjU1ZGU5MmRjNmRhODY2NTUyM2I2YmRjYzEiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImF1dGh3cmFwcGVyLmJhY2tlbmRzLmF1dGguTXlCYWNrZW5kIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-09-10 05:44:51');
INSERT INTO `django_session` VALUES ('mw9d4b4xv0eix0mn3ks8b5kt8kv1qgsq', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-08-20 00:58:31');
INSERT INTO `django_session` VALUES ('n3hao2w8dnvv0n94gwcrzm1noq0pfuca', 'MjFlMTNlODgwZThlMGM3MmUwMjBhZjY3YmU0YjU3MTQ0YWY4OTYzNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoicGVyc29uYWxjZW50ZXIuYmFja2VuZHMuYXV0aC5NeUJhY2tlbmQiLCJfc2Vzc2lvbl9leHBpcnkiOjAsImNhcnRfaXRlbV9jb3VudCI6MCwidXNlcl9jaGVja291dF9pZCI6MSwiX2F1dGhfdXNlcl9oYXNoIjoiNjYwNDFhM2ZkMmU4MmZmNmNkYmVhMmQ5YTE1ZDJjMTQyZmFlYWE3NyJ9', '2017-05-17 11:22:53');
INSERT INTO `django_session` VALUES ('ng2dps0jqutixjavpxcow49d697jsso7', 'ZjQxODkyNDQyMGNmYzM4YjEwNjlmMjg0NTZiMmU5ZGViOWMzYTA0Yjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6InBlcnNvbmFsY2VudGVyLmJhY2tlbmRzLmF1dGguV2VjaGF0QmFja2VuZCIsIndlY2hhdF9pZCI6MzQsIl9hdXRoX3VzZXJfaGFzaCI6IjYyYWJhYjg5NGNhNDgzNzcwNTYzMDUyMTk5YTFiZGU4N2ZjYzQ4MzciLCJfYXV0aF91c2VyX2lkIjoiNSIsImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-06-06 13:53:11');
INSERT INTO `django_session` VALUES ('nwt810arddivp88y92962jaw5qc60m8n', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2016-12-31 07:27:35');
INSERT INTO `django_session` VALUES ('o7cbo3o49a81e7783tv6jvoi14s2jmpm', 'NWE5MzJlNzYzYjI4ZDQwNTYzMDZmMjAwODE2OTQ3NDc1MDY1ZTcwZjp7Il9sYW5ndWFnZSI6InpoLWNuIiwiX2F1dGhfdXNlcl9oYXNoIjoiNWY3Njc2MTQ0ODc1ZTM2NTVkZTkyZGM2ZGE4NjY1NTIzYjZiZGNjMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImF1dGh3cmFwcGVyLmJhY2tlbmRzLmF1dGguTXlCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJjYXJ0X2l0ZW1fY291bnQiOjB9', '2017-09-10 15:11:39');
INSERT INTO `django_session` VALUES ('ocsiavcyof1xquwyahec060nlwc4xnm8', 'MDRlOTQxNTg4YTBmYmU2OGUwYmQzYTUxOTNkYzgwZDA0ZjNlNjcwNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY2MDQxYTNmZDJlODJmZjZjZGJlYTJkOWExNWQyYzE0MmZhZWFhNzciLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6InBlcnNvbmFsY2VudGVyLmJhY2tlbmRzLmF1dGguTXlCYWNrZW5kIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2016-12-25 13:57:28');
INSERT INTO `django_session` VALUES ('octmhyxqlvnu8z61apx1cp4lnebtnl9v', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2016-12-31 12:34:59');
INSERT INTO `django_session` VALUES ('pcp2vmg6iu9aiv7v04nbot6ir522f9e5', 'M2ZjY2I3NjQ5ZmY4OWJjNzE1ZDQxNDVjMzNmN2Y1YzZhN2NiMzQ1ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjY2MDQxYTNmZDJlODJmZjZjZGJlYTJkOWExNWQyYzE0MmZhZWFhNzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJwZXJzb25hbGNlbnRlci5iYWNrZW5kcy5hdXRoLk15QmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-06-17 08:14:22');
INSERT INTO `django_session` VALUES ('pfw0jvhwvzlla4unb62fgep3vm096htg', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-04-03 14:21:42');
INSERT INTO `django_session` VALUES ('qfmvmh01t8m845e5b0jb4fiimvehh0k7', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2016-12-31 09:22:33');
INSERT INTO `django_session` VALUES ('rjsfftq72m8y587w93m7wqzxg43242nz', 'Yzg4OTcxNzJhYmI5Y2E4YzIzN2U2ZTA3YWE5OWQ0MjA2ZTNhYTM3NTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwib3JkZXJfaWQiOjQsIl9hdXRoX3VzZXJfYmFja2VuZCI6InBlcnNvbmFsY2VudGVyLmJhY2tlbmRzLmF1dGguTXlCYWNrZW5kIiwiX3Nlc3Npb25fZXhwaXJ5IjowLCJjYXJ0X2l0ZW1fY291bnQiOjEsIl9hdXRoX3VzZXJfaGFzaCI6IjY2MDQxYTNmZDJlODJmZjZjZGJlYTJkOWExNWQyYzE0MmZhZWFhNzciLCJjYXJ0X2lkIjo2fQ==', '2017-04-08 01:24:03');
INSERT INTO `django_session` VALUES ('sjeqy5f9rzbojusr8nsokxjt3ypcd4t9', 'MTY2NTA3ZDgzNTUzNGI2ZGZiOTNhZDJhYjk1M2IxN2Q3MTg1Yzk2MTp7Il9sYW5ndWFnZSI6ImVuIiwiZGphbmdvX2xhbmd1YWdlIjoiJ2VuLXVzJyIsImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-09-02 16:11:23');
INSERT INTO `django_session` VALUES ('tecei179ci86tqvztbz1ylvlk4cjgixt', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2016-12-31 08:06:35');
INSERT INTO `django_session` VALUES ('tmgytnlyftpo21slbmjlrwlhwelixd4t', 'MzQ1ZGFhODI4MmJhZjY0MDliYWU1MDRiMTM3ZDUxZDQ2NjZjMWMzMTp7IndlY2hhdF9pZCI6MzMsImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-06-04 16:28:57');
INSERT INTO `django_session` VALUES ('u3eweedwzhahc56vbxgak5qz0p9b85zd', 'YmYyMTQ0MTcwZjIyZGI0NDliNTMwYmY4MTExN2M4NjRiYTc4NjEzNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjVmNzY3NjE0NDg3NWUzNjU1ZGU5MmRjNmRhODY2NTUyM2I2YmRjYzEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhdXRod3JhcHBlci5iYWNrZW5kcy5hdXRoLk15QmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2017-09-03 12:49:00');
INSERT INTO `django_session` VALUES ('un54vbat7hmne1djjsfn5ik35yuzijtk', 'Yzc1YjI3M2ZmMjI1ZDNjYzQ0ZGQ2ZmY1NWNhYjYyYzQ2NTUxMGRmODp7IndlY2hhdF9pZCI6MjIsImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-06-04 15:41:51');
INSERT INTO `django_session` VALUES ('vcutk0zjamsouc4gryijrri9lip2ioct', 'MDRlOTQxNTg4YTBmYmU2OGUwYmQzYTUxOTNkYzgwZDA0ZjNlNjcwNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY2MDQxYTNmZDJlODJmZjZjZGJlYTJkOWExNWQyYzE0MmZhZWFhNzciLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6InBlcnNvbmFsY2VudGVyLmJhY2tlbmRzLmF1dGguTXlCYWNrZW5kIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2016-12-31 09:45:49');
INSERT INTO `django_session` VALUES ('vg4tisklo1jikky9dk70oe0v3ne2kq2n', 'NjA5ZTNiNDdkNjA1MmMzNTAzOWQyOTZkYTgwZjQxMzA1ZDg5YTg4Nzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6InBlcnNvbmFsY2VudGVyLmJhY2tlbmRzLmF1dGguV2VjaGF0QmFja2VuZCIsIndlY2hhdF9pZCI6MjAsIl9hdXRoX3VzZXJfaGFzaCI6IjhlZjZmMjBmNGMxNDZmZjgzYTM3YTM4NzQ5NTBkMDUwZTNhZGNlMjUiLCJfYXV0aF91c2VyX2lkIjoiMTEiLCJjYXJ0X2l0ZW1fY291bnQiOjB9', '2016-12-17 03:17:48');
INSERT INTO `django_session` VALUES ('viqf1vdnjyuy1qkgibkrkhtyk3gy9s7w', 'YWJkODQ4MWIxMDgzMTJkZWRkOTVmYmJjNjM3NDcwYTNiNDE4N2MxODp7IndlY2hhdF9pZCI6MywiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-07-29 06:47:13');
INSERT INTO `django_session` VALUES ('vjz4tm17s2cld1a003ctto3nqljbx4sh', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-05-14 07:10:57');
INSERT INTO `django_session` VALUES ('vnugdsu4n3nr6nhipsnkdthhiq5r2h6i', 'MjY5YWMxYWRkZTU4OGY5Mjg0NmRmNzg5YjJlZWFkNDNjZTQ0ODBmZDp7IndlY2hhdF9pZCI6MzEsImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-06-04 16:19:03');
INSERT INTO `django_session` VALUES ('wqidb306nb87rpnshc78d5csn2iwly3i', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-07-29 02:10:42');
INSERT INTO `django_session` VALUES ('wx1nn9k8ussx1ehcvlc3npbxmoqrcvdr', 'YTVhN2MyZmU2N2JjOWJhOTk1ZGVhZjUwZjNmOTRlODQ5ZTA2NWUxMDp7Il9hdXRoX3VzZXJfaGFzaCI6ImY4Njg0ZTE0OGExZDk1ODQ2OWE2NDVjZDNmYzNlMjQxNTQwZTM4YzEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJwZXJzb25hbGNlbnRlci5iYWNrZW5kcy5hdXRoLldlY2hhdEJhY2tlbmQiLCJfYXV0aF91c2VyX2lkIjoiNCJ9', '2016-12-14 07:42:08');
INSERT INTO `django_session` VALUES ('x8f9w7j0urip5it20wc140z4px2nrjeq', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-08-28 16:19:03');
INSERT INTO `django_session` VALUES ('xbl1acf1lj33ekw1x0p3xz7q6szwp1r9', 'MDgzOWY3Zjg5MzYzYjQ3N2E2NTllNjY3NDkwOWNjZDQxMTdmODU4NTp7Il9hdXRoX3VzZXJfaGFzaCI6IjNkMTg4Yjk1Njc0Mjc4ODM2N2RmNDZkYmI3ZGMyZWY0ODNlNmM4ZDMiLCJfYXV0aF91c2VyX2lkIjoiNDMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhdXRod3JhcHBlci5iYWNrZW5kcy5hdXRoLk15QmFja2VuZCIsImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-07-30 06:04:41');
INSERT INTO `django_session` VALUES ('ybysfhnicka5iv6u9q3r2h5oj6jsg3fd', 'NzQ2ZjhlMDZlNTBlODFmY2YzYjljNzBlZWEwNDczODEzZWYyMTcwYTp7Il9hdXRoX3VzZXJfaGFzaCI6IjVmNzY3NjE0NDg3NWUzNjU1ZGU5MmRjNmRhODY2NTUyM2I2YmRjYzEiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImF1dGh3cmFwcGVyLmJhY2tlbmRzLmF1dGguTXlCYWNrZW5kIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-07-23 13:42:19');
INSERT INTO `django_session` VALUES ('yd7gfbdwy49oucqp838s6v4uv53afzjw', 'NzQ2ZjhlMDZlNTBlODFmY2YzYjljNzBlZWEwNDczODEzZWYyMTcwYTp7Il9hdXRoX3VzZXJfaGFzaCI6IjVmNzY3NjE0NDg3NWUzNjU1ZGU5MmRjNmRhODY2NTUyM2I2YmRjYzEiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImF1dGh3cmFwcGVyLmJhY2tlbmRzLmF1dGguTXlCYWNrZW5kIiwiY2FydF9pdGVtX2NvdW50IjowfQ==', '2017-09-04 07:35:06');
INSERT INTO `django_session` VALUES ('yte9dpadio8jrv4fizgi30ott6ukvsu3', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-07-27 15:59:48');
INSERT INTO `django_session` VALUES ('z7gpdp65h85t69woohs6sxmwgnn1n7px', 'MjE4OWZhZTYyODk3MzU0NmMxYzU2YmU0MDA3ZmExYWQ5MjkyMjY4Njp7ImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-07-29 02:06:02');
INSERT INTO `django_session` VALUES ('zr8920luc8u5l96lo0fxuqcqbxn8v4f0', 'NjY3ZDUxYTIxMjdmOTk4NDBmNDVmYzMxYzcyOTIzMzNlODIzYmI4MDp7IndlY2hhdF9pZCI6MjgsImNhcnRfaXRlbV9jb3VudCI6MH0=', '2017-06-04 16:08:11');

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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_dailyinspection
-- ----------------------------
INSERT INTO `inspection_dailyinspection` VALUES ('1', '[u\'2\']', '杨志想', 'dailyinspection/people/2017-08-14-15-08-26-1502042224227609564.jpg', 'dailyinspection/people/2017-08-14-15-08-26-none-banner1.png', '2017-08-14', 'people', '2017-08-26 06:38:16', '4号液压车损坏', '1', '立即要求相关人员进行整改', 'uncompleted', '2017-08-27 03:21:07');
INSERT INTO `inspection_dailyinspection` VALUES ('2', '[u\'3\']', '赵云', 'dailyinspection/people/2017-08-14-15-27-11-chemicals.jpg', '', '2017-08-14', 'people', '2017-08-26 06:38:16', '', '1', '', 'uncompleted', '2017-08-26 06:38:38');
INSERT INTO `inspection_dailyinspection` VALUES ('5', '[u\'1\']', '张飞', 'dailyinspection/people/2017-08-22-15-09-58-1502042158235115305.jpg', 'dailyinspection/people/2017-08-22-15-09-58-1502042215046268724.jpg', '2017-07-01', 'people', '2017-08-26 06:38:16', '', '1', '', 'uncompleted', '2017-08-26 06:38:38');
INSERT INTO `inspection_dailyinspection` VALUES ('6', '[u\'3\']', '杨志想', 'dailyinspection/people/2017-08-23-13-43-25-automotive.jpg', '', '2017-08-14', 'people', '2017-08-26 06:38:16', '', '1', '', 'uncompleted', '2017-08-26 06:38:38');
INSERT INTO `inspection_dailyinspection` VALUES ('7', '[u\'2\']', '杨志想', 'dailyinspection/people/2017-08-23-13-58-08-projects-and-energy.jpg', 'dailyinspection/people/2017-08-23-13-58-08-chemicals.jpg', '2017-08-30', 'device', '2017-08-26 06:38:16', '52K14散拍未并拍', '1', '立即要求相关人员进行整改', 'completed', '2017-08-27 03:26:35');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_forklift
-- ----------------------------
INSERT INTO `inspection_forklift` VALUES ('1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_forklift_image
-- ----------------------------
INSERT INTO `inspection_forklift_image` VALUES ('1', 'inspection/forklift/None-banner1.png', '1');
INSERT INTO `inspection_forklift_image` VALUES ('2', 'inspection/forklift/None-banner2.png', '1');

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
  `accessories` varchar(30) NOT NULL,
  `name` varchar(30) NOT NULL,
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
  `image` varchar(100),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_officeinspection
-- ----------------------------
INSERT INTO `inspection_officeinspection` VALUES ('8', 'yes', 'ChuangKe', '2017-08-10 13:56:46', '2017-08-12 13:08:56', '想1', 'yes', 'E:\\Computer\\virtualenv\\zakkabag\\zakkabag\\static_in_env\\media_root\\inspection\\create.jpg');
INSERT INTO `inspection_officeinspection` VALUES ('13', 'yes', 'Jinqiao', '2017-08-10 14:07:58', '2017-08-10 15:34:44', '', 'yes', null);
INSERT INTO `inspection_officeinspection` VALUES ('14', 'yes', 'Hetian', '2017-08-10 15:19:58', '2017-08-10 15:20:29', '', 'yes', null);
INSERT INTO `inspection_officeinspection` VALUES ('15', 'no', 'HZ', '2017-08-10 15:40:41', '2017-08-11 13:47:22', '', 'yes', null);
INSERT INTO `inspection_officeinspection` VALUES ('16', 'yes', 'Beijing', '2017-08-11 13:45:16', '2017-08-11 13:45:16', '', 'yes', null);
INSERT INTO `inspection_officeinspection` VALUES ('17', 'yes', 'ChuangKe', '2017-08-11 13:57:23', '2017-08-11 13:57:23', '', 'yes', null);

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
INSERT INTO `inspection_shelf` VALUES ('1', '横梁式', '3', '1', '1', '1', '1', '1');
INSERT INTO `inspection_shelf` VALUES ('2', '横梁式', '2', '2', '2', '2', '2', '1');

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
  `comments` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_shelf_inspection
-- ----------------------------

-- ----------------------------
-- Table structure for `inspection_shelf_inspection_record`
-- ----------------------------
DROP TABLE IF EXISTS `inspection_shelf_inspection_record`;
CREATE TABLE `inspection_shelf_inspection_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `use_condition` varchar(30) NOT NULL,
  `is_locked` tinyint(1) NOT NULL,
  `check_person` varchar(30) NOT NULL,
  `gradient` decimal(20,1) NOT NULL,
  `comments` longtext NOT NULL,
  `shelf_id` int(11) NOT NULL,
  `shelf_inspection_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `inspection_shelf_inspec_shelf_id_175de8b1_fk_inspection_shelf_id` (`shelf_id`),
  KEY `inspection_shelf_inspection_record_8b1352f8` (`shelf_inspection_id`),
  CONSTRAINT `inspection_shelf_inspec_shelf_id_175de8b1_fk_inspection_shelf_id` FOREIGN KEY (`shelf_id`) REFERENCES `inspection_shelf` (`id`),
  CONSTRAINT `i_shelf_inspection_id_4fdf5361_fk_inspection_shelf_inspection_id` FOREIGN KEY (`shelf_inspection_id`) REFERENCES `inspection_shelf_inspection` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inspection_shelf_inspection_record
-- ----------------------------

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
INSERT INTO `newsletter_article` VALUES ('1', 'Chemicals', '<p><img alt=\"\" src=\"http://localhost:8000/media/article/chemicals.jpg\" /></p>\r\n\r\n<p>The special characteristics of chemical industry make its logistics challenging. Leveraging our professional team, comprehensive licenses, strict HSEQ system and emergency response centers, we offer green supply chain solutions for sustainable growth.<br />\r\nWe offer the following services for both dangerous and non-dangerous goods:</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p><strong>&middot;&nbsp;</strong>International Logistics Services</p>\r\n\r\n<p><strong>&middot;&nbsp;</strong>Shuttle Road Transport Services</p>\r\n\r\n<p><strong>&middot;&nbsp;</strong>Long Haul and Regional Distribution</p>\r\n\r\n<p><strong>&middot;&nbsp;</strong>Warehousing and Sample Management</p>\r\n\r\n<p><strong>&middot;&nbsp;</strong>Multimodal Transportation</p>\r\n\r\n<p><strong>&middot;&nbsp;</strong>ISO TANK and Liquid Chemical Tanker Services</p>\r\n\r\n<p><strong>&middot;&nbsp;</strong>Dry Bulk Bag Container Transport</p>\r\n\r\n<p><strong>&middot;&nbsp;</strong>Repackaging, Refilling and Hazardous Waste Transport</p>\r\n', '2017-04-30 04:47:01', 'The special characteristics of chemical industry make its logistics challenging.', 'article/chemicals.jpg');
INSERT INTO `newsletter_article` VALUES ('2', 'Projects and Energy', '<p><img alt=\"\" src=\"http://localhost:8000/media/article/projects-and-energy.jpg\" style=\"height:260px; width:670px\" /></p>\r\n\r\n<p>Our project logistics footprint spans over 100 countries and regions. We have handled transportation of materials and equipment for over 400 large-scale projects from infrastructure construction, mining, to oil and gas exploitation, new energy etc. We leverage our professional logistics solutions and strong overseas operational capabilities to provide our clients turn-key project logistics solutions. Our services include:</p>\r\n\r\n<p>　　<strong>&middot;&nbsp;</strong>One-stop Project Logistics Solution Design</p>\r\n\r\n<p>　　<strong>&middot;&nbsp;</strong>Road Survey</p>\r\n\r\n<p>　　<strong>&middot;&nbsp;</strong>Door to Door Project Logistics Services</p>\r\n\r\n<p>　　<strong>&middot;&nbsp;</strong>Warehousing and Packaging</p>\r\n\r\n<p>　　<strong>&middot;&nbsp;</strong>Charter Flight and Vessel Charter Services</p>\r\n\r\n<p>　　<strong>&middot;&nbsp;</strong>Customs Clearance and Documentation</p>\r\n\r\n<p>　　<strong>&middot;&nbsp;</strong>Large and Ultra-large Equipment Trucking</p>\r\n\r\n<p>　　<strong>&middot;&nbsp;</strong>Cargo Tracking</p>\r\n\r\n<p>　　<strong>&middot;&nbsp;</strong>Relevant Policies and Regulations Consultation of Destination Countries</p>\r\n', '2017-04-30 05:51:19', 'Our project logistics footprint spans over 100 countries and regions. ', 'article/projects-and-energy.jpg');
INSERT INTO `newsletter_article` VALUES ('3', 'Automotive', '<p>We provide tailor-made logistics solutions to the world&rsquo;s leading automotive manufacturers.Our services include:</p>\r\n\r\n<p><img alt=\"\" src=\"http://localhost:8000/media/article/2016-cmef-in-shanghai.jpg\" style=\"height:260px; width:670px\" /></p>\r\n\r\n<p><strong>Inbound Logistics</strong></p>\r\n\r\n<p>　　<strong>&middot;&nbsp;</strong>International Transportation of Raw Materials</p>\r\n\r\n<p>　　<strong>&middot;&nbsp;</strong>Milk-run and JIT Transportation</p>\r\n\r\n<p>　　<strong>&middot;&nbsp;</strong>Inbound logistics</p>\r\n\r\n<p>　　<strong>&middot;&nbsp;</strong>VMI</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p><strong>Site Logistics</strong></p>\r\n\r\n<p>　　<strong>&middot;&nbsp;</strong>Line feeding and Empty Appliance Management</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p><strong>Outbound &nbsp;Logistics</strong></p>\r\n\r\n<p>　　<strong>&middot;&nbsp;</strong>Finished car transportation by container ship and ro-ro vessel</p>\r\n\r\n<p>　　<strong>&middot;&nbsp;</strong>Spare Parts Warehousing and Distribution</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p><strong>Value-added Services</strong></p>\r\n\r\n<p>　　<strong>&middot;&nbsp;</strong>Repacking, Sequencing, Quality Control, Kitting, etc.</p>\r\n', '2017-04-30 07:23:09', 'Automotive', 'article/2016-cmef-in-shanghai.jpg');

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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of newsletter_banner
-- ----------------------------
INSERT INTO `newsletter_banner` VALUES ('1', 'banner/None-banner1.png', 'banner1', 'banner1', '0');
INSERT INTO `newsletter_banner` VALUES ('2', 'banner/None-banner2.png', 'banner2', 'banner2', '0');
INSERT INTO `newsletter_banner` VALUES ('3', 'banner/None-banner3.png', 'banner3', 'banner3', '0');
INSERT INTO `newsletter_banner` VALUES ('4', 'banner/automotive.jpg', 'automotive', 'automotive', '1');
INSERT INTO `newsletter_banner` VALUES ('6', 'banner/chemicals.jpg', 'chemicals', 'chemicals', '1');
INSERT INTO `newsletter_banner` VALUES ('7', 'banner/project-and-energy.jpg', 'project and energy', 'project and energy', '1');

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
  CONSTRAINT `orders_order_cart_id_2f8c40e6_fk_carts_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `carts_cart` (`id`),
  CONSTRAINT `orders_order_user_id_5bd989c5_fk_orders_usercheckout_id` FOREIGN KEY (`user_id`) REFERENCES `orders_usercheckout` (`id`),
  CONSTRAINT `orders_orde_billing_address_id_5afecadd_fk_orders_useraddress_id` FOREIGN KEY (`billing_address_id`) REFERENCES `orders_useraddress` (`id`),
  CONSTRAINT `orders_ord_shipping_address_id_491fafef_fk_orders_useraddress_id` FOREIGN KEY (`shipping_address_id`) REFERENCES `orders_useraddress` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of orders_order
-- ----------------------------
INSERT INTO `orders_order` VALUES ('1', '5.99', '8.14', '1', '2', '2', '1', 'completed', null);
INSERT INTO `orders_order` VALUES ('3', '5.99', '10.29', '1', '5', '2', '1', 'completed', null);
INSERT INTO `orders_order` VALUES ('4', '5.99', '17.81', null, '6', null, null, 'created', null);
INSERT INTO `orders_order` VALUES ('5', '5.99', '17.81', '1', '7', '2', '1', 'completed', null);
INSERT INTO `orders_order` VALUES ('6', '5.99', '65.12', '1', '8', '2', '1', 'paid', '1');
INSERT INTO `orders_order` VALUES ('7', '5.99', '17.81', '1', '9', '2', '1', 'paid', '1');
INSERT INTO `orders_order` VALUES ('8', '5.99', '328.49', '1', '11', '2', '1', 'paid', '1');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of orders_useraddress
-- ----------------------------
INSERT INTO `orders_useraddress` VALUES ('1', 'billing', 'Guiqiao Road', 'Shanghai', 'China', '201000', '1');
INSERT INTO `orders_useraddress` VALUES ('2', 'shipping', 'Guiqiao Road', 'Shanghai', 'China', '201000', '1');

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
  CONSTRAINT `orders_usercheckout_user_id_685d2891_fk_personalcenter_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `personalcenter_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of orders_usercheckout
-- ----------------------------
INSERT INTO `orders_usercheckout` VALUES ('1', 'bin.he@live.com', '1', null);

-- ----------------------------
-- Table structure for `personalcenter_myuser`
-- ----------------------------
DROP TABLE IF EXISTS `personalcenter_myuser`;
CREATE TABLE `personalcenter_myuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `account_type` varchar(50) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `username` varchar(30) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `nickname` varchar(30) NOT NULL,
  `sex` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `personalcenter_myuser_phone_29f4f60_uniq` (`phone`),
  UNIQUE KEY `personalcenter_myuser_email_5027c3b4_uniq` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of personalcenter_myuser
-- ----------------------------
INSERT INTO `personalcenter_myuser` VALUES ('1', 'pbkdf2_sha256$20000$haGuqKzqnL2R$Zql5oZUvkHLP3NNHXgFbSm2f3RIKs4P+oULR6iV4Txc=', '2017-07-09 12:17:40', '1', 'username', '1', '1', '2016-11-27 16:02:00', 'bin.he1@live.com', 'bin', 'He', '13709874567', 'bhe001', 'upload\\1029263936-0.jpg', '2020-06-19', 'hebinn', 'female');
INSERT INTO `personalcenter_myuser` VALUES ('6', 'pbkdf2_sha256$20000$Hm7FiRMcvmvE$u1PvtAQ2Gh9XCr5WMqsMYGKYM/xLTTwzKQaWduq16uI=', '2016-12-03 04:40:20', '0', 'username', '1', '0', '2016-12-02 03:46:21', 'bin.he2@live.com', '', '', '13813456789', 'bhe003', '1', '1970-01-01', '', '');
INSERT INTO `personalcenter_myuser` VALUES ('79', 'pbkdf2_sha256$20000$l7QCC4ZEIeqw$pdGyYqTl6/IylzLEuczjqNAmSOsQAyJx1PL1NW9qRek=', '2017-07-09 12:17:08', '1', 'username', '1', '1', '2017-06-25 03:00:00', 'bin.he3@live.com', '', '', '+8613500000000', '13500000000', 'profile/13500000000/1314078420523_000-79.jpg', null, '', 'male');
INSERT INTO `personalcenter_myuser` VALUES ('87', 'pbkdf2_sha256$20000$hHkKSuGduEnT$cmlvEMlsySArO934C9RCbKkFBglDUMa7lRkXvoqmWYs=', '2017-07-09 01:59:00', '0', 'phone', '1', '0', '2017-07-09 01:56:00', 'bin.he4@live.com', '', '', '+8613113331112', '13113331112', '', '2017-07-09', '', 'male');
INSERT INTO `personalcenter_myuser` VALUES ('88', 'pbkdf2_sha256$20000$kJ28HXb04UUc$BOfMOxRrN/uPz8MF3oQ09jdMiOv+mezZAu5du37XKAo=', '2017-07-09 02:00:00', '0', 'phone', '1', '0', '2017-07-09 01:59:00', 'bin.he5@live.com', '', '', '+8613514341234', '13514341234', '', '2017-07-09', '', 'male');
INSERT INTO `personalcenter_myuser` VALUES ('89', 'pbkdf2_sha256$20000$SA0Ij6lnwgHw$ldIt72dBe2XHGgXEwF4ID04GOq560Str7srU6eW8QhI=', '2017-07-09 12:14:31', '1', 'mail', '1', '1', '2017-07-09 11:38:27', 'bin.he@live.cn', '', '', '+8613500010001', 'bhe0011', '', null, '', 'male');
INSERT INTO `personalcenter_myuser` VALUES ('91', 'pbkdf2_sha256$20000$3wpDyvZE2HF2$Z52MbKYsyvv+O0WP3N3rosY0nAYRXdRjI3aOpMiwa8E=', null, '0', 'phone', '1', '0', '2017-07-09 12:21:21', null, '', '', '+8613400010002', '+8613400010002', '', null, '', 'male');
INSERT INTO `personalcenter_myuser` VALUES ('92', 'pbkdf2_sha256$20000$RpAoE9qPrHQH$0x0NPfwuP0ns8Ks8AW4nndDwZdXq8/MegGJhJPYCjmY=', '2017-07-09 12:35:32', '0', 'phone', '1', '0', '2017-07-09 12:35:10', null, 'Bin', 'He', '+8613500010002', '+8613500010002', 'upload\\1314078420523_000.jpg', '2017-07-09', 'Bin', 'male');

-- ----------------------------
-- Table structure for `personalcenter_myuser_groups`
-- ----------------------------
DROP TABLE IF EXISTS `personalcenter_myuser_groups`;
CREATE TABLE `personalcenter_myuser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myuser_id` (`myuser_id`,`group_id`),
  KEY `personalcenter_myuser_groups_group_id_3355744a_fk_auth_group_id` (`group_id`),
  CONSTRAINT `personalcenter_myuser_groups_group_id_3355744a_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `personalcenter_myu_myuser_id_95893d9_fk_personalcenter_myuser_id` FOREIGN KEY (`myuser_id`) REFERENCES `personalcenter_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of personalcenter_myuser_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `personalcenter_myuser_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `personalcenter_myuser_user_permissions`;
CREATE TABLE `personalcenter_myuser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myuser_id` (`myuser_id`,`permission_id`),
  KEY `personalcenter_myuse_permission_id_8493acd_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `personalcenter_myuse_permission_id_8493acd_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `personalcenter_my_myuser_id_5a6ea16b_fk_personalcenter_myuser_id` FOREIGN KEY (`myuser_id`) REFERENCES `personalcenter_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of personalcenter_myuser_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `personalcenter_userprofile`
-- ----------------------------
DROP TABLE IF EXISTS `personalcenter_userprofile`;
CREATE TABLE `personalcenter_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `score` decimal(10,0) NOT NULL,
  `level` decimal(10,0) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `personalcenter_user_user_id_19709a27_fk_personalcenter_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `personalcenter_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of personalcenter_userprofile
-- ----------------------------
INSERT INTO `personalcenter_userprofile` VALUES ('1', '41', '5', '1');
INSERT INTO `personalcenter_userprofile` VALUES ('2', '0', '0', '92');

-- ----------------------------
-- Table structure for `personalcenter_wechatuserprofile`
-- ----------------------------
DROP TABLE IF EXISTS `personalcenter_wechatuserprofile`;
CREATE TABLE `personalcenter_wechatuserprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `openid` varchar(120) DEFAULT NULL,
  `unionid` varchar(120) DEFAULT NULL,
  `privilege` varchar(120) DEFAULT NULL,
  `headimgurl` varchar(500) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `country` varchar(45) DEFAULT NULL,
  `language` varchar(45) DEFAULT NULL,
  `nickname` varchar(120) DEFAULT NULL,
  `sex` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `personalcenter_wech_user_id_1d7ddc75_fk_personalcenter_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `personalcenter_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of personalcenter_wechatuserprofile
-- ----------------------------

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
) ENGINE=InnoDB AUTO_INCREMENT=167 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of phone_login_phonetoken
-- ----------------------------
INSERT INTO `phone_login_phonetoken` VALUES ('103', '+8613500192123', '354704', '2017-07-15 03:22:44', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('104', '+8613500192123', '691647', '2017-07-15 03:25:04', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('105', '+8613500192123', '901950', '2017-07-15 03:26:54', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('106', '+8613600000000', '357804', '2017-07-15 03:32:22', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('107', '+8613600000000', '720228', '2017-07-15 03:34:20', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('108', '+8613700000000', '486309', '2017-07-15 03:38:35', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('109', '+8613700000000', '937193', '2017-07-15 04:49:00', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('110', '+8613800000000', '944619', '2017-07-15 04:49:10', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('111', '+8613800000000', '214420', '2017-07-15 04:50:41', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('112', '+8613900000000', '784843', '2017-07-15 04:50:52', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('113', '+8613900000000', '756298', '2017-07-15 04:51:13', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('114', '+8613900000001', '140298', '2017-07-15 04:51:46', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('115', '+8613900000002', '540486', '2017-07-15 04:52:40', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('116', '+8613900000003', '637857', '2017-07-15 04:54:01', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('117', '+8613800000004', '586648', '2017-07-15 04:56:39', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('118', '+8613800000005', '030949', '2017-07-15 05:30:09', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('119', '+861380000006', '456750', '2017-07-15 05:32:20', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('120', '+861380000007', '894069', '2017-07-15 05:32:30', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('121', '+8613800000007', '573658', '2017-07-15 05:32:41', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('122', '+8613800000008', '684667', '2017-07-15 05:33:48', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('123', '+8613800000009', '887897', '2017-07-15 05:34:47', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('124', '+8613900000001', '967929', '2017-07-15 05:36:28', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('125', '+8613900000011', '083794', '2017-07-15 05:37:11', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('126', '+8613900000021', '111907', '2017-07-15 05:37:36', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('127', '+8613900000030', '679362', '2017-07-15 05:48:01', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('128', '+8613900000040', '570082', '2017-07-15 05:49:42', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('129', '+8613900000050', '939429', '2017-07-15 05:50:35', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('130', '+1350000000', '812709', '2017-07-15 05:53:35', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('131', '+13500000000', '260907', '2017-07-15 05:53:49', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('132', '+9613500000000', '571512', '2017-07-15 05:54:01', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('133', '+8613500000000', '523881', '2017-07-15 05:54:13', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('134', '+861350000000', '602426', '2017-07-15 05:54:24', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('135', '+8613500000001', '361742', '2017-07-15 05:54:49', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('136', '+8613600000000', '820061', '2017-07-15 05:56:26', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('137', '+13700000000', '561992', '2017-07-15 05:57:33', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('138', '+8613700000000', '648410', '2017-07-15 05:57:42', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('139', '+8613700000000', '614960', '2017-07-15 06:28:17', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('140', '+8613700000000', '942279', '2017-07-15 06:28:34', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('141', '+8613600000000', '735101', '2017-07-15 06:28:43', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('142', '+8613700000000', '952153', '2017-07-15 06:31:43', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('143', '+8613600000000', '275179', '2017-07-15 06:31:50', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('144', '+8613600000000', '225364', '2017-07-15 06:32:47', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('145', '+8613600000000', '405889', '2017-07-15 06:33:13', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('146', '', '999790', '2017-07-15 09:20:41', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('147', '', '201609', '2017-07-15 09:22:35', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('148', '+NoneNone', '489816', '2017-07-15 09:59:14', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('149', '+8613900000000', '366488', '2017-07-15 09:59:31', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('150', '', '598875', '2017-07-15 10:02:06', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('151', '', '877113', '2017-07-15 10:02:13', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('152', '+8613901234567', '527864', '2017-07-15 10:02:39', '1', '1');
INSERT INTO `phone_login_phonetoken` VALUES ('153', '+NoneNone', '681308', '2017-07-15 10:12:28', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('154', '+8613400010003', '426659', '2017-08-07 15:29:50', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('155', '+8613400010003', '235585', '2017-08-07 15:30:03', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('156', '+8613400010003', '566843', '2017-08-07 15:30:05', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('157', '+8613400010003', '121402', '2017-08-07 15:30:09', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('158', '+8613400010003', '372110', '2017-08-07 15:30:12', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('159', '+8613400010003', '021063', '2017-08-07 15:30:19', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('160', '+8613400010003', '861273', '2017-08-07 15:30:25', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('161', '+8613400010003', '148703', '2017-08-07 15:30:35', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('162', '+8613400010003', '644305', '2017-08-07 15:30:42', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('163', '+8613676541234', '107172', '2017-08-07 15:30:57', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('164', '+8613676541234', '329842', '2017-08-07 15:31:30', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('165', '+8613900000001', '875948', '2017-08-07 15:58:39', '0', '0');
INSERT INTO `phone_login_phonetoken` VALUES ('166', '+8613900000001', '692398', '2017-08-07 15:59:16', '0', '0');

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
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;

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
  CONSTRAINT `registration_regist_user_id_3f7685bb_fk_personalcenter_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `personalcenter_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of registration_registrationprofile
-- ----------------------------

-- ----------------------------
-- Table structure for `threadedcomments_comment`
-- ----------------------------
DROP TABLE IF EXISTS `threadedcomments_comment`;
CREATE TABLE `threadedcomments_comment` (
  `comment_ptr_id` int(11) NOT NULL,
  `title` longtext NOT NULL,
  `tree_path` varchar(500) NOT NULL,
  `last_child_id` int(11) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`comment_ptr_id`),
  KEY `D07a26747879ea7075f204c806cdecd4` (`last_child_id`),
  KEY `th_parent_id_151fb735_fk_threadedcomments_comment_comment_ptr_id` (`parent_id`),
  CONSTRAINT `D07a26747879ea7075f204c806cdecd4` FOREIGN KEY (`last_child_id`) REFERENCES `threadedcomments_comment` (`comment_ptr_id`),
  CONSTRAINT `threadedcomments_c_comment_ptr_id_636575de_fk_django_comments_id` FOREIGN KEY (`comment_ptr_id`) REFERENCES `django_comments` (`id`),
  CONSTRAINT `th_parent_id_151fb735_fk_threadedcomments_comment_comment_ptr_id` FOREIGN KEY (`parent_id`) REFERENCES `threadedcomments_comment` (`comment_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of threadedcomments_comment
-- ----------------------------
