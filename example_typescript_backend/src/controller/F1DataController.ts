import "reflect-metadata";
import { NextFunction, Request, Response } from "express";

import { F1DataService } from '../service/F1DataService';

export class F1DataController extends F1DataService
{
    getAll(request: Request, response: Response, next: NextFunction)
    {
      return this.getAllDrivers();
    }
    refresh(request: Request, response: Response, next: NextFunction)
    {
        return this.refreshDrivers();
    }
}
