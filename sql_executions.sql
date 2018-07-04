BEGIN
	rdsadmin.rdsadmin_util.alter_supplemental_logging('ADD');	
END;

BEGIN
	rdsadmin.rdsadmin_util.alter_supplemental_logging('ADD','PRIMARY KEY');
END;

BEGIN
	rdsadmin.rdsadmin_util.set_configuration('archivelog retention hours',24);
END;

SELECT supplemental_log_data_min, force_logging FROM v$database;

SELECT supplemental_log_data_min MIN, 
supplemental_log_data_pk PK, 
supplemental_log_data_ui UI, 
supplemental_log_data_fk FK,
supplemental_log_data_all "ALL" 
FROM v$database;

