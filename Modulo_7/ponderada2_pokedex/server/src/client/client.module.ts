import { Module } from '@nestjs/common';
import { ClientService } from './client.service';
import { ClientController } from './client.controller';
import { User } from 'src/entities/user.entity';
import { Pokemons } from 'src/entities/pokemons.entity';
import { TypeOrmModule } from '@nestjs/typeorm';

@Module({
  controllers: [ClientController],
  providers: [ClientService],
  exports: [ClientService],
  imports: [TypeOrmModule.forFeature([User, Pokemons])],
})
export class ClientModule {}
