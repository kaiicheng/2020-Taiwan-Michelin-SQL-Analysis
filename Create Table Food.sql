CREATE TABLE `food` (  
	`id` varchar(32) NOT NULL,  
	`p_type` varchar(10) NOT NULL,  
	`s_area_id` varchar(32) NOT NULL,  
	`comment_count` bigint(20) DEFAULT NULL,  
	`post_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',  
	`title` text NOT NULL,  
	`author` text,  
	`content` longtext,  
	`page_url` longtext NOT NULL,  
	`sentiment` varchar(1) DEFAULT NULL,  
	PRIMARY KEY (`id`),  
	KEY `ts_page_content_area_index` (`s_area_id`),  
	KEY `ts_page_content_post_index` (`post_time`),  
	KEY `ts_page_content_area_post_index` (`s_area_id`,`post_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
