#include <iostream>
#include <regex>
#include <string>

std::string toLower(const std::string& str) {
    std::string lowerStr = str;
    std::transform(lowerStr.begin(), lowerStr.end(), lowerStr.begin(), 
                   [](unsigned char c){ return std::tolower(c); });
    return lowerStr;
}

int main() {
    std::regex comandoUm("\\b(busque|vai?\\s+at[eé]|v[aá]\\s+para)\\s+(.+)\\b");
    std::regex comandoDois("\\b(ajuda|o\\s+que\\s+voc[eê]\\s+pode\\s+fazer)\\b");
    std::regex comandoTres("\\b(voc[eê]\\s+est[aá]\\s+ocupado|vai\\s+demorar|onde\\s+voc[eê]\\s+est[aá])\\b");

    std::string input;

    while (true) {
        std::cout << "\n\nDigite seu comando: \n -> \033[36m";
        std::getline(std::cin, input);
        std::cout << "\033[32m";

        std::string lowerInput = toLower(input);
        std::smatch matches;

        if (std::regex_search(lowerInput, matches, comandoUm) && matches.size() > 1) {
            std::cout <<"\n" << matches[2] << " fica na prateleira dois, estou indo até lá...\n";
        } else if (std::regex_search(lowerInput, matches, comandoDois)) {
            std::cout << "\nComandos aceitos:\n" << std::endl;
            std::cout << "1. [busque/vá até/vá para] <nome do produto>"<< std::endl;
            std::cout << "    -> Busca o produto requisitado\n"<< std::endl;
            std::cout << "2. [ajuda/o que você pode fazer?]"<< std::endl;
            std::cout << "    -> Mostra esse diálogo\n"<< std::endl;
            std::cout << "3. [Você esta ocupado?/vai demorar?/onde voce está?]"<< std::endl;
            std::cout << "    -> Mostra o estado atual do robô\n"<< std::endl;
        } else if (std::regex_search(lowerInput, matches, comandoTres)) {
            std::cout << "\nO Vallet está ocupado no momento...\n-> Sua requisição está na posição [3] da fila de espera.";
        } else {
            std::cout << "\nUhmm... não conheço esse comando :( \n Você pode digitar 'ajuda' para ver a lista de comandos possíveis\n";
        }
        std::cout << "\033[0m";
    }

    return 0;
}
