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
      .then(async (fromRunpy: number) => {
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
          gender: Number(gender) ? 'mulher' : 'homem',
        };
      })
      .catch((err) => {
        throw new InternalServerErrorException(err);
      });
  }

  async getAllRuns() {
    return await this.RunsRepository.find();
  }

  async getStatistics() {
    let responseObj = {
      maleVsFemale: [{ name: 'male', value: 0 },{ name: 'female', value: 0 }],
      ageVsIncome: [],
    };
    await this.RunsRepository.find({
      order: {
        age: 'ASC',
      },
    }).then((runs) => {
      //GENERATE THE MALEFEMALE STATISTIC
      // --------------------------------------------------
      runs.forEach((run) => {
        if (run.gender === 1) {
          responseObj.maleVsFemale[1].value += 1;
        } else {
          responseObj.maleVsFemale[0].value += 1;
        }
      });
      // --------------------------------------------------
      //GENERATE THE agevsincome STATISTIC
      // --------------------------------------------------
      const agesAlreadyAdded = [];
      runs.forEach((run) => {
        if (agesAlreadyAdded.includes(run.age)) {
          responseObj.ageVsIncome.forEach((ageVsIncome) => {
            if (ageVsIncome.age === run.age) {
              ageVsIncome.amountOfMeans += 1;
              ageVsIncome.income =
                (ageVsIncome.income * (ageVsIncome.amountOfMeans - 1) +
                  run.income) /
                ageVsIncome.amountOfMeans;
            }
          });
        } else {
          responseObj.ageVsIncome.push({
            name: run.age,
            age: run.age,
            income: run.income,
            amountOfMeans: 1,
          });
          agesAlreadyAdded.push(run.age);
        }
      });
      // --------------------------------------------------
    });
    return responseObj;
  }

  getHistoric() {
    return this.RunsRepository.find({
      order: {
        id: 'desc',
      },
      take: 10,
    });
  }
}
