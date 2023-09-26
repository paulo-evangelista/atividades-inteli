import {
  Controller,
  Get,
  Post,
  Body,
  Patch,
  Param,
  Delete,
  Req,
  UseGuards,
  HttpCode,
} from '@nestjs/common';
import { ClientService } from './client.service';
import { Request } from 'express';
import { AuthGuard } from 'src/auth/auth.guard';

@Controller('client')
export class ClientController {
  constructor(private readonly clientService: ClientService) {}

  @UseGuards(AuthGuard)
  @Get('/testJWT')
  testJWT(@Req() request: any) {
    return `JWT is working and you're signed in as the user: ${request.user.username}`;
  }

  @HttpCode(200)
  @Post('/run')
  async run(@Body() body: any) {
    console.log(body)
    console.log(`new run sent: ${body.age}, ${body.income}, ${body.gender}`)
    return await this.clientService.run(body.age, body.income, body.gender);
  }

  @HttpCode(200)
  @Get('/getAllRuns')
  async getAllRuns() {
    return await this.clientService.getAllRuns();
  }
}
