import {
  Injectable,
  UnauthorizedException,
  BadRequestException,
  Inject,
} from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { User } from 'src/entities/users.entity';
import { JwtService } from '@nestjs/jwt';
import * as bcrypt from 'bcrypt';


@Injectable()
export class AuthService {
  constructor(
    @InjectRepository(User)
    private UserRepository: Repository<User>,
    private jwtService: JwtService,
  ) {}

  async register(username: string, pass: string): Promise<any> {
    const user = await this.UserRepository.findOneBy({ username: username });
    if (user) {
      throw new BadRequestException('user already exists');
    }
    const salt = await bcrypt.genSalt();
    const hashedPass = await bcrypt.hash(pass, salt);
    return this.UserRepository.insert({ username, password: hashedPass });
  }

  async signIn(username: string, pass: string): Promise<any> {
    const user = await this.UserRepository.findOneBy({username: username});
    if (!bcrypt.compare(pass, user.password)) {
      throw new UnauthorizedException();
    }
    const { password, ...result } = user;
    const payload = { sub: user.id, username: user.username };
    return {
      token: await this.jwtService.signAsync(payload),
    };
  }
}
