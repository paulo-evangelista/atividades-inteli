import { Module } from '@nestjs/common';
import { AuthController } from './auth.controller';
import { AuthService } from './auth.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { User } from 'src/entities/users.entity';
import { jwtConstants } from './constants';
import { JwtModule } from '@nestjs/jwt';

@Module({
  controllers: [AuthController],
  providers: [AuthService],
  imports: [TypeOrmModule.forFeature([User]), JwtModule.register({
    global: true,
    secret: jwtConstants.secret,
    signOptions: { expiresIn: '12h' },
  }),],
})
export class AuthModule {}
