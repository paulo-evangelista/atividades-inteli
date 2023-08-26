import { Controller, Get, UseGuards } from '@nestjs/common';
import { Post, Body, HttpStatus, HttpCode } from '@nestjs/common';
import { AuthService } from './auth.service';
import { AuthGuard } from './auth.guard';

@Controller('auth')
export class AuthController {
  constructor(private authService: AuthService) {}

  @HttpCode(HttpStatus.OK)
  @Post('login')
  signIn(@Body() signInDto: Record<string, any>) {
    return this.authService.logIn(signInDto.username, signInDto.password);
  }

  @UseGuards(AuthGuard)
  @Get('protected')
  protectedResource() {
    return 'JWT is working!';
  }
}
