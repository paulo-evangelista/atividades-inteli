import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class Pokemons {

  @PrimaryGeneratedColumn()
  id: number;

    @Column()
    ownerId: string;

  @Column()
  nickname: string;
  
  @Column()
  species: string;
  
  @Column()
  imgURL: string;
  
  @Column()
  number: string;

  @Column("text", {array: true})
  type: string[];

}
