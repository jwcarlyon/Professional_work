import * as driversActionTypes from './driversActionTypes';

export function getDriverStats(driverName)
{
    return{
        type: driversActionTypes.DRIVERS__GET_STATS,
        driverName: driverName
    };
}
export function updateStats(stats)
{
    return{
        type: driversActionTypes.DRIVERS__GET_STATS_SUCCESS,
        stats: stats
    };
}

export function updateStatsWithBlank()
{
    return{
        type: driversActionTypes.DRIVERS__GET_STATS_FAILED
    };
}
