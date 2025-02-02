import { useState } from "react";

const AM_RATE = 0.08;

const SalaryForm = () => {
    const [salary, setSalary] = useState("");
    const [tax, setTax] = useState("");
    const [deductions, setDeductions] = useState("");
    const [netIncome, setNetincome] = useState(null);

    const handleSubmit = (e) => {
        e.preventDefault();

        const grossIncome = Number(salary);
        const taxPercentage = Number(tax)
        const deductionAmount = Number(deductions)

        const amContribution = grossIncome  * AM_RATE;
        const taxableIncome = grossIncome - amContribution - deductionAmount;
        const calculatedNetIncome = taxableIncome * (1 - (taxPercentage / 100));

        setNetincome(calculatedNetIncome.toFixed(2));
    }

    const handleReset = () => {
        setSalary("");
        setTax("");
        setDeductions("");
        setNetincome("");
    }

    return (
        <div className="flex flex-col items-center gap-4">
            <form onSubmit={handleSubmit} className="flex flex-col gap-4">
                <div className="flex items-center">
                    <label htmlFor="salary" className="w-32">Bruttoløn:</label>
                    <input
                        type="number"
                        name="salary"
                        id="salary"
                        className="border rounded flex-1"
                        value={salary}
                        onChange={(e) => setSalary(e.target.value)}
                    />
                </div>

                <div className="flex items-center">
                    <label htmlFor="tax" className="w-32">Skatteprocent:</label>
                    <input
                        type="number"
                        name="tax"
                        id="tax"
                        className="border rounded flex-1"
                        value={tax}
                        onChange={(e) => setTax(e.target.value)}
                    />
                </div>

                <div className="flex items-center">
                    <label htmlFor="deductions" className="w-32">Fradrag:</label>
                    <input
                        type="number"
                        name="deductions"
                        id="deductions"
                        className="border rounded flex-1"
                        value={deductions}
                        onChange={(e) => setDeductions(e.target.value)}
                    />
                </div>

                <div className="flex justify-between">
                <button
                    type="submit"
                    className="w-32 bg-sky-500 text-white py-2 px-4 rounded hover:bg-sky-600 mx-auto">
                    Beregn
                </button>
                <button
                    onClick={handleReset}
                    className="w-32 bg-sky-500 text-white py-2 px-4 rounded hover:bg-sky-600 mx-auto">
                    Nulstil
                </button>
                </div>
                
            </form>

            {netIncome !== null && (
                <div className="mt-4 p-4 bg-sky-300 rounded shadow-md">
                    <h2 className="text-xl">Nettoløn:</h2>
                    <p className="text-2xl">{netIncome} DKK</p>
                </div>
            )}
        </div>
    )
}

export default SalaryForm;