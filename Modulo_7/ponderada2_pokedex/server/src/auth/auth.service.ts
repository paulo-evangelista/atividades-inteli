import { Injectable, UnauthorizedException, BadRequestException, HttpStatus } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { User } from '../entities/user.entity';
import { JwtService } from '@nestjs/jwt';
import * as bcrypt from 'bcrypt';
import { error } from 'console';
interface userTypes {
  username: string;
  password: string;
}

@Injectable()
export class AuthService {
  constructor(
    @InjectRepository(User)
    private usersRepository: Repository<User>,
    private jwtService: JwtService,
  ) {}

  async logIn(username: string, password: string): Promise<any> {
    console.log("someone is trying to log in!\nuser:", username,"\npassword:", password)
    if (!username || !password) throw new BadRequestException(HttpStatus.BAD_REQUEST, "some value seems to be missing")
    const res = await this.usersRepository.findOneBy({ username: username });
  console.log(res)
    if (res && (await bcrypt.compare(password, res.password))) {
      console.log(res);
      const payload = { sub: res.id, username: res.username };
      return {
        access_token: await this.jwtService.signAsync(payload),
        userId: res.id,
      };
    } else throw new UnauthorizedException('Wrong username or password');
  }
}
