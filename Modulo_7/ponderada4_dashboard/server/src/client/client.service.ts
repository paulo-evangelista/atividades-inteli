import {
  Inject,
  Injectable,
  InternalServerErrorException,
} from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { User } from 'src/entities/users.entity';
import { Repository } from 'typeorm';
import { spawn } from 'child_process';
import { Runs } from 'src/entities/runs.entity';

@Injectable()
export class ClientService {
  constructor(
    @InjectRepository(Runs)
    private RunsRepository: Repository<Runs>,
  ) {}

  async run(age, income, gender) {
    const runModel = new Promise((resolve, reject) => {
      const py = spawn('python', ['./AI/run.py', age, income, gender]);
      py.stdout.on('data', function (data) {
        resolve(data.toString());
      });
      py.stderr.on('data', (data) => {
        reject(data.toString());
      });
    });

    return await runModel
      .then(async (fromRunpy: number)  =>  {
        await this.RunsRepository.insert({
          age: age,
          income: income,
          gender: gender,
          result: fromRunpy,
        });
        return {
          result: Number(fromRunpy),
          age: Number(age),
          income: Number(income),
          gender: Number(gender) ? "mulher"  : "homem" 
        }
      })
      .catch((err) => {
        throw new InternalServerErrorException(err);
      });
  }

  async getAllRuns() {
    return await this.RunsRepository.find();
  }
}
