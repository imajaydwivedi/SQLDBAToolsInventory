exec sp_helpdb [TivoSQLInventory_Ajay]
exec sp_helpdb [TivoSQLInventory]

-- Get Latest Full Backup
SELECT TOP (1)
	bmf.physical_device_name
FROM msdb.dbo.backupmediafamily AS bmf
	INNER JOIN msdb.dbo.backupset AS bs ON bmf.media_set_id = bs.media_set_id
WHERE bs.type='D' and database_name = 'TivoSQLInventory'
ORDER BY bs.backup_finish_date DESC

-- Create/Replace/Restore Database
declare @backpFile varchar(255);
set @backpFile = 'G:\MSSQLData\SQL2016_Backup\TivoSQLInventory\FULL\TivoSQLInventory_FULL_20181207_213000.bak';
restore database  [TivoSQLInventory_Dev] from disk = @backpFile
	with move 'TivoSQLInventory' to 'F:\MSSQLData\SQL2016_Data\TivoSQLInventory_Dev.mdf',
		move 'TivoSQLInventory_log' to 'F:\MSSQLData\SQL2016_Data\TivoSQLInventory_Dev_log.ldf',
		stats = 5
		,replace
go

/*
alter database [TivoSQLInventory_Ajay] set single_user with rollback immediate
go
declare @backpFile varchar(255);
set @backpFile = 'G:\MSSQLData\SQL2016_Backup\TivoSQLInventory\FULL\TivoSQLInventory_FULL_20181207_213000.bak';
restore database  [TivoSQLInventory_Ajay] from disk = @backpFile
	with move 'TivoSQLInventory' to 'F:\MSSQLData\SQL2016_Data\TivoSQLInventory_Ajay.mdf',
		move 'TivoSQLInventory_log' to 'F:\MSSQLData\SQL2016_Data\TivoSQLInventory_Ajay_log.ldf',
		stats = 5
		,replace
go
*/

use [TivoSQLInventory]
go
ALTER TABLE [dbo].[Instance] WITH CHECK ADD CONSTRAINT [FK_Instance_ServerID]
   FOREIGN KEY([ServerID]) REFERENCES [dbo].[Server] ([ServerID])

GO

ALTER TABLE [dbo].[Databases] WITH CHECK ADD CONSTRAINT [FK_Databases_InstanceId]
   FOREIGN KEY([InstanceId]) REFERENCES [dbo].[Instance] ([InstanceID])

GO

ALTER TABLE [dbo].[BackupSchedule] WITH CHECK ADD CONSTRAINT [FK_BackupSchedule_InstanceId]
   FOREIGN KEY([InstanceId]) REFERENCES [dbo].[Instance] ([InstanceID])

GO

ALTER TABLE [dbo].[BackupHistory] WITH CHECK ADD CONSTRAINT [FK_BackupHistory_DatabaseId]
   FOREIGN KEY([DatabaseId]) REFERENCES [dbo].[Databases] ([DatabaseId])

GO
ALTER TABLE [dbo].[BackupHistory] WITH CHECK ADD CONSTRAINT [FK_BackupHistory_InstanceId]
   FOREIGN KEY([InstanceId]) REFERENCES [dbo].[Instance] ([InstanceID])

GO

ALTER TABLE [dbo].[CommandQueue] WITH CHECK ADD CONSTRAINT [FK_CommandQueue_DatabaseId]
   FOREIGN KEY([DatabaseId]) REFERENCES [dbo].[Databases] ([DatabaseId])

GO

ALTER TABLE [dbo].[CommandQueue] WITH CHECK ADD CONSTRAINT [FK_CommandQueue_InstanceId]
   FOREIGN KEY([InstanceId]) REFERENCES [dbo].[Instance] ([InstanceID])

GO

-- Add Primary Key Constraint on dbo.[CommandQueue]
ALTER TABLE [dbo].[CommandQueue] ADD ID BIGINT IDENTITY(1,1);

ALTER TABLE [dbo].[CommandQueue]
	ADD CONSTRAINT PK_CommandQueue_ID PRIMARY KEY CLUSTERED (ID);  
GO

-- Add Primary Key Constraint on dbo.[CommandQueue]
ALTER TABLE [dbo].[Logging]
	ADD CONSTRAINT PK_Logging_LogId PRIMARY KEY CLUSTERED (LogId);  
GO 

CREATE NONCLUSTERED INDEX NCI_Server_ServerName ON dbo.Server(Server)
GO