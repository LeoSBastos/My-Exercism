=begin
Write your code for the 'Matrix' exercise in this file. Make the tests in
`matrix_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/matrix` directory.
=end

class Matrix
  def initialize(matrix)
    @matrixRows = matrix.split("\n")
  end

  def rows
    @rows = []
    for row in @matrixRows
      @rows.push(row.split.map { |el| el.to_i })
    end
    @rows
  end

  def columns
    @columns = []
    rows[0].length.times { @columns.push([]) }
    for row in rows
      row.length.times { |i| @columns[i].push(row[i]) }
    end
    @columns
  end
end
