import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import helmet from 'helmet';

const corsOptions = {
  origin: 'http://localhost:3000',
  credentials: true,

}

async function bootstrap() {  
  const app = await NestFactory.create(AppModule);  
  app.use(helmet())
  app.enableCors(corsOptions)
  await app.listen(4000);
}

bootstrap();
