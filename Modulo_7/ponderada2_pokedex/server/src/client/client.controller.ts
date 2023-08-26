import { Controller, Get, Req, Post, Delete, Put, HttpCode, HttpStatus, HttpException, BadRequestException } from '@nestjs/common';
import { ClientService } from './client.service';
import { Request, response, Response } from 'express';

interface signIn extends Request {
  body: {
    username: string;
    password: string;
  };
}
interface getPokemons extends Request {
  body: {
    userId: string;
  };
}
interface deletePokemon extends Request {
  body: {
    pokemonId: number;
  };
}

interface editNickname extends Request {
  body: {
    pokemonId: number;
    nickname: string | '';
  };
}

interface addPokemon extends Request {
  body: {
    pokemon: string | number;
    userId: string;
  };
}

@Controller('client')
export class ClientController {
  constructor(private readonly clientService: ClientService) {}

  @Get('getAll')
  getAll() {
    return this.clientService.getAll();
  }

  @Post('signin')
  async signIn (@Req() request: signIn, response: Response) {
    const { username, password } = request.body;
    return await this.clientService.signIn({ username, password });
    
  }

  @Post('getPokemons')
  getPokemons(@Req() request: getPokemons) {
    console.log(request.body)
    const { userId } = request.body;
    console.log(userId,"\n\n")
    return this.clientService.getPokemons(userId);
  }
  @Post('deletePokemon')
  deletePokemon(@Req() request: deletePokemon) {
    console.log("alguem quer deletar! -> pokemonID: ", request.body)
    const { pokemonId } = request.body;
    return this.clientService.deletePokemon(pokemonId);
  }
  @Post('editNickname')
  editNickname(@Req() request: editNickname) {
    const { pokemonId, nickname } = request.body;
    return this.clientService.editNickname({ pokemonId, nickname });
  }
  @Put('addPokemon')
  addPokemon(@Req() request: addPokemon) {
    const { pokemon, userId } = request.body;
    return this.clientService.addPokemon(pokemon, userId);
  }
}
