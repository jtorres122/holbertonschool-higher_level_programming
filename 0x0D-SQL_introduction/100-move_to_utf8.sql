-- Script converts database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8m COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8 COLLATE utf8mb4_unicode_ci;
