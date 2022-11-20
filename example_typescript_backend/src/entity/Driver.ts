import { Entity, PrimaryColumn, Column } from "typeorm"

@Entity()
export class Driver
{
    @PrimaryColumn()
    driverId: string;
    @Column()
    permanentNumber: number;
    @Column()
    code: string;
    @Column()
    url: string;
    @Column()
    givenName: string;
    @Column()
    familyName: string;
    @Column()
    dateOfBirth: string;
    @Column()
    nationality: string;
}
