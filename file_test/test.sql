CREATE TABLE `user_address_ysq` (
  `address_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `name` varchar(30)  COMMENT '收货人姓名',
  `password` varchar(20) COMMENT '密码',
  `phone` varchar(20)  COMMENT '联系电话',
  `detail` varchar(255) COMMENT '详细地址',
  PRIMARY KEY (`address_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户收货';
