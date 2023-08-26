import { Injectable, HttpException, HttpStatus, BadRequestException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { User } from '../entities/user.entity';
import { Pokemons } from '../entities/pokemons.entity';
import * as bcrypt from 'bcrypt';
import axios from 'axios';
interface userTypes {
  username: string;
  password: string;
}

interface editNickname {
  pokemonId: number;
  nickname: string | '';
}

@Injectable()
export class ClientService {
  constructor(
    @InjectRepository(User)
    private usersRepository: Repository<User>,
    @InjectRepository(Pokemons)
    private pokemonsRepository: Repository<Pokemons>,
  ) {}

    async getAll() {
      return this.usersRepository.findBy({})
    }

  async signIn({ username, password }: userTypes) {
    console.log("Alguém está tentando se registrar!\nuser:", username,"\npassword:", password)
    const res = await this.usersRepository.findOneBy({ username: username });
    console.log(res)
    if (!res) {
      console.log("o usuario não existe ainda... continuando")
      const hashedPassword = await bcrypt.hash(password, 10);
      const dbRes = await this.usersRepository.insert({
        username: username,
        password: hashedPassword,
      });
      if (dbRes) {
      console.log("sucesso, usuario criado com a senha criptografada: ", hashedPassword)
      return "created"
      }
    } else {
      throw new BadRequestException(HttpStatus.BAD_REQUEST, "user already exists")
    }
  }

  async getPokemons(userId: string) {
    console.log(userId, "Wants his pokemons!")
    const dbRes = await this.pokemonsRepository.find({order:{number: "asc"}, where:{ ownerId: userId}  });
    dbRes.sort(function(a, b) {
      let aa = parseInt(a.number);
      let bb = parseInt(b.number);
      return aa-bb
      }
    );
    return dbRes
  }
  async deletePokemon(pokemonId: number) {
    console.log("---------------->", pokemonId)
    return await this.pokemonsRepository.delete({id: pokemonId});
  }
  async editNickname({pokemonId, nickname}: editNickname) {
    if (nickname === '') {
      return await this.pokemonsRepository.update(pokemonId,{ nickname: "" });
    }
    return await this.pokemonsRepository.update(pokemonId,{ nickname: nickname });
  }

  async addPokemon(pokemon: string | number, userId: string) {
    try {
      const apiRes = await axios.get(
        `https://pokeapi.co/api/v2/pokemon/${pokemon}`,
      );

      const pokemonTypes = [];

      for (let i in apiRes.data.types) {
        pokemonTypes.push(apiRes.data.types[i].type.name);
      }

      const pkmObj = {
        ownerId: userId,
        nickname: '',
        species: apiRes.data.name,
        type: pokemonTypes,
        imgURL: apiRes.data.sprites.front_default,
        number: apiRes.data.id,
      };

      await this.pokemonsRepository.insert(pkmObj);

      return pkmObj;
    } catch (err) {
      return err;
    }
  }

  // return await this.usersRepository.findBy({ username: username });
}
