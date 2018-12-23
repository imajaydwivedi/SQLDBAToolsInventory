-- Standalone Server
select * from dbo.Server s where s.IsStandaloneServer = 1;
select * from dbo.Instance i where i.IsStandaloneInstance = 1;

-- SqlClusters
select * from dbo.Server as s where s.IsSqlCluster = 1;
select * from dbo.Instance as i where i.IsSqlCluster = 1;

-- AG Listeners
select * from dbo.Server as s where s.IsAG = 1;
select * from dbo.Instance as i where i.IsAGListener = 1;

-- Servers involved in Mirroring
select * from dbo.Instance as i where i.HasOtherHASetup = 1 AND HARole like 'Mirror%'

-- Servers involved in Replication
select * from dbo.Instance as i where i.HasOtherHASetup = 1 AND HARole like 'Replication%'

-- Servers involved in Log Shipping
select * from dbo.Instance as i where i.HasOtherHASetup = 1 AND HARole like 'Log%'

-- Find All Supported SqlInstances to be Monitored
select * from dbo.Instance i

