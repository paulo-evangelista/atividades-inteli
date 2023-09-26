
import { Entity, Column, PrimaryGeneratedColumn, CreateDateColumn } from 'typeorm';

@Entity()
export class Runs {
  @PrimaryGeneratedColumn()
  id: number;

  @CreateDateColumn()
  created_at: Date;

  @Column()
  age: number;

  @Column("float")
  income: number;

  @Column("int2")
  gender: number;

  @Column("float")
  result: number;
}
