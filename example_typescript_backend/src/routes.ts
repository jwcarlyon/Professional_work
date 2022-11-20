import { F1DataController } from "./controller/F1DataController";
import { UserController } from "./controller/UserController";

export const Routes = [{
    method: "get",
    route: "/users",
    controller: UserController,
    action: "all"
}, {
    method: "get",
    route: "/users/:id",
    controller: UserController,
    action: "one"
}, {
    method: "post",
    route: "/users",
    controller: UserController,
    action: "save"
}, {
    method: "delete",
    route: "/users/:id",
    controller: UserController,
    action: "remove"
}, {
    method: "get",
    route: "/f1/all",
    controller: F1DataController,
    action: "getAll"
}, {
    method: "get",
    route: "/f1/refresh",
    controller: F1DataController,
    action: "refreshDrivers"
}];
