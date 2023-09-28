import { Module } from '@nestjs/common';
import { AppController } from '../app.controller';
import { AppService } from './app.service';
import { ClientModule } from './client/client.module';
import { AuthModule } from './auth/auth.module';
import { TypeOrmModule } from '@nestjs/typeorm';
import { User } from './entities/users.entity';
import { Runs } from './entities/runs.entity';

@Module({
  imports: [ClientModule, AuthModule,
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: 'postgres',
      port: 5432,
      username: 'user',
      password: 'password',
      database: 'mydb',
      entities: [User, Runs],
      synchronize: true,
    }),],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
