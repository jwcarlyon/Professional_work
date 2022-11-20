import { Driver } from "../entity/Driver";

export type F1DriversDataResponse =
{
    MRData: F1ResponseCountainer;
};
export type F1ResponseCountainer =
{
    xmlns: string;
    series: string;
    url: string;
    limit: number;
    offset: number;
    total: number;
    DriverTable: F1DriverTable;
};
export type F1DriverTable =
{
    season: string;
    Drivers: Driver[];
};
