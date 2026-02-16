=begin
Write your code for the 'Rna Transcription' exercise in this file. Make the tests in
`rna_transcription_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/rna-transcription` directory.
=end


class Complement

    def self.transformar(letter)
        case letter
            when "G"
                "C"
            when "C"
                "G"
            when "T"
                "A"
            when "A"
                "U"
        end
    end
    def self.of_dna(dna)
        if(dna.length == 1)
            self.transformar(dna)
        else 
            letters = []
            for letter in dna.split("")
                letters.push(self.transformar(letter))
            end
            letters.join
        end
    end
end
