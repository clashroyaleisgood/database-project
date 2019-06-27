delete from playlist;
delete from song;
delete from series;
delete from album;
delete from artist;

insert into artist values('周杰倫', '杰威爾音樂');
insert into artist values('米津玄師', 'Sony Music Records');
insert into artist values('華晨宇', '天娛傳媒');

insert into album values('周杰倫的床邊故事', 2016, '周杰倫');
insert into album values('哎呦，不錯哦', 2014, '周杰倫');
insert into album values('BOOTLEG', 2017, '米津玄師');
insert into album values('Bremen', 2015, '米津玄師');
insert into album values('異類', 2015, '華晨宇');
insert into album values('卡西莫多的禮物', 2014, '華晨宇');

insert into series values('中文', '中文歌曲');
insert into series values('日文', '日文歌曲');

insert into song values(default, '周杰倫 Jay Chou【前世情人 Lover From Previous Life】Official MV', 'j9k3liT2MLo', '周杰倫', '周杰倫的床邊故事', '中文', 207);
insert into song values(default, '周杰倫Jay Chou X aMEI【不該 Shouldnt Be】Official MV', '_VxLOj3TB5k', '周杰倫', '周杰倫的床邊故事', '中文', 293);
insert into song values(default, '周杰倫 Jay Chou【愛情廢柴 Failure at love】Official MV', '2kdYSeoHChg', '周杰倫', '周杰倫的床邊故事', '中文', 279);
insert into song values(default, '周杰倫 Jay Chou 【Now You See Me】Official MV (120s)', 'LbUKhXO2oCs', '周杰倫', '周杰倫的床邊故事', '中文', 124);
insert into song values(default, '周杰倫 Jay Chou【聽見下雨的聲音 Rhythm of the Rain】Official MV', 'zqKoXPHhmsM', '周杰倫', '哎呦，不錯哦', '中文', 283);
insert into song values(default, '周杰倫 Jay Chou【算什麼男人 What Kind of Man】Official MV (ft. 林依晨)', 'v489sYYjtHI', '周杰倫', '哎呦，不錯哦', '中文', 287);
insert into song values(default, '周杰倫 Jay Chou【手寫的從前 Handwritten Past】Official MV', 'TMB6-YflpA4', '周杰倫', '哎呦，不錯哦', '中文', 294);
insert into song values(default, '周杰倫 Jay Chou【天涯過客 Passer-by】Official MV', '-gJzlOJ0Zoo', '周杰倫', '哎呦，不錯哦', '中文', 252);
insert into song values(default, '米津玄師 MV「LOSER」', 'Dx_fKPBPYUI', '米津玄師', 'BOOTLEG', '日文', 241);
insert into song values(default, '米津玄師 MV「Lemon」', 'SX_ViT4Ra7k', '米津玄師', NULL, '日文', 274);
insert into song values(default, '米津玄師 MV「orion」', 'lzAyrgSqeeE', '米津玄師', 'BOOTLEG', '日文', 290);
insert into song values(default, '米津玄師 MV「海の幽霊」Spirits of the Sea', '1s84rIhPuhk', '米津玄師', NULL, '日文', 255);
insert into song values(default, '米津玄師 MV「ピースサイン」Kenshi Yonezu / Peace Sign', '9aJVr5tTTWk', '米津玄師', 'BOOTLEG', '日文', 264);
insert into song values(default, '米津玄師 MV「Flowerwall」', 'Y4_vXzyOJHE', '米津玄師', 'Bremen', '日文', 309);

insert into playlist values(default, 1);
insert into playlist values(default, 2);
insert into playlist values(default, 3);	
insert into playlist values(default, 4);