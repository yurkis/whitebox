
-- Table: session
CREATE TABLE session ( 
    SID               PRIMARY KEY
                      NOT NULL
                      UNIQUE,
    user     CHAR     NOT NULL,
    expires  DATETIME NOT NULL,
    is_admin BOOLEAN  NOT NULL
                      DEFAULT ( 0 ) 
);


-- Table: db_info
CREATE TABLE db_info ( 
    db_ver 
);

INSERT INTO [db_info] ([db_ver]) VALUES (0);
