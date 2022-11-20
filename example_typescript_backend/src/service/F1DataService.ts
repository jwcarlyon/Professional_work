import axios from 'axios';
import { createConnection, getRepository } from "typeorm"

import ErrorHandler from '../models/ErrorHandler';
import { F1DriversDataResponse, F1ResponseCountainer, F1DriverTable } from '../models/F1DriversDataResponse';
import { Driver } from '../entity/Driver';

export class F1DataService
{
    private driverRepository = getRepository(Driver);

    async getAllDrivers()
    {
        console.log("All drivers request");
        return this.driverRepository.find();
    }
    async refreshDrivers()
    {
        try {
            const { data, status } = await axios.get<F1DriversDataResponse>(
                'http://ergast.com/api/f1/2022/drivers.json', {
                    headers: { Accept: 'application/json', },
                },
            );
            this.loadDriversFromResponse(data.MRData.DriverTable.Drivers);
            // console.log(JSON.stringify(data, null, 4));
            console.log('response status is: ', status);
            return "Driver repository refreshed.";
        } catch (error) {
            if (axios.isAxiosError(error))
            {
                console.log('error message: ', error.message);
                return error.message;
            } else {
                console.log('unexpected error: ', error);
                return 'An unexpected error occurred';
            }
        }
    }
    private async loadDriversFromResponse(driver_list : Driver[])
    {
        driver_list.map(async driver =>this.driverRepository.save(driver))
    }
}
